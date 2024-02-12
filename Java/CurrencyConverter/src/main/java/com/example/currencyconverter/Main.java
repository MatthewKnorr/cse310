package com.example.currencyconverter;

import javafx.application.Application;
import javafx.beans.property.SimpleStringProperty;
import javafx.geometry.Insets;
import javafx.scene.Scene;
import javafx.scene.control.*;
import javafx.scene.control.cell.PropertyValueFactory;
import javafx.scene.layout.*;
import javafx.scene.paint.Color;
import javafx.stage.Stage;

import java.util.Arrays;
import java.util.List;

// Entry Point
public class Main extends Application {
    private static double exchangeRate = 0.000;
    @Override
    public void start(Stage primaryStage) {
        primaryStage.setTitle("Currency Converter");

        Label amountLabel = new Label("Enter Amount:");
        TextField amountField = new TextField();
        Label exchangeRateLabel = new Label("Exchange Rate:");
        Label rateValueLabel = new Label(String.valueOf(exchangeRate));

        ComboBox<String> currencyComboBox = new ComboBox<>();
        List<String> currencies = Arrays.asList(
                "Select a currency", "$USD - United States Dollar", "€EUR - Euro", "$AUD - Australian Dollar", "£GBP - British Pound Sterling", "¥JPY - Japanese Yen", "$CAD - Canadian Dollar", "$NZD - New Zealand Dollar", "₪ILS - Israeli Shekel", "$HKD - Hong Kong Dollar", "krNOK - Norwegian Krone"
        );
        currencyComboBox.getItems().addAll(currencies);
        currencyComboBox.setValue("Select a currency");

        TableView<Conversion> tableView = new TableView<>();
        TableColumn<Conversion, String> amountColumn = new TableColumn<>("Amount");
        TableColumn<Conversion, String> convertedColumn = new TableColumn<>("Converted");
        tableView.getColumns().addAll(amountColumn, convertedColumn);

        amountColumn.setCellValueFactory(new PropertyValueFactory<>("amount"));
        convertedColumn.setCellValueFactory(new PropertyValueFactory<>("convertedAmount"));


        Label conversionLabel = new Label();

        currencyComboBox.setOnAction(e -> {
            String selectedCurrency = currencyComboBox.getValue();
            exchangeRate = getExchangeRate(selectedCurrency);
            rateValueLabel.setText(String.valueOf(exchangeRate));
            tableView.getItems().clear();
            populateTable(tableView, amountField.getText(), selectedCurrency);
            updateConversionLabel(amountField.getText(), selectedCurrency, conversionLabel);
        });

        amountField.setTextFormatter(new TextFormatter<>(change ->
                (change.getControlNewText().matches("\\d*\\.?\\d*")) ? change : null));

        amountField.textProperty().addListener((observable, oldValue, newValue) -> {
            tableView.getItems().clear();
            populateTable(tableView, newValue, currencyComboBox.getValue());
            updateConversionLabel(newValue, currencyComboBox.getValue(), conversionLabel);
        });

        GridPane gridPane = new GridPane();
        gridPane.setPadding(new Insets(20));
        gridPane.setHgap(10);
        gridPane.setVgap(10);

        BackgroundFill backgroundFill = new BackgroundFill(Color.rgb(30, 30, 30), CornerRadii.EMPTY, Insets.EMPTY);
        Background background = new Background(backgroundFill);
        gridPane.setBackground(background);

        amountLabel.setTextFill(Color.WHITE);
        exchangeRateLabel.setTextFill(Color.WHITE);
        rateValueLabel.setTextFill(Color.WHITE);
        currencyComboBox.setStyle("-fx-background-color: white; -fx-text-fill: black;");
        tableView.setStyle("-fx-background-color: #2f2f2f; -fx-text-fill: white;");
        amountField.setStyle("-fx-background-color: #2f2f2f; -fx-text-fill: white;");
        conversionLabel.setStyle("-fx-text-fill: white");

        gridPane.add(amountLabel, 0, 0);
        gridPane.add(amountField, 1, 0);
        gridPane.add(exchangeRateLabel, 0, 1);
        gridPane.add(rateValueLabel, 1, 1);
        gridPane.add(conversionLabel, 0, 3, 2, 1);
        gridPane.add(currencyComboBox, 0, 4, 2, 1);
        gridPane.add(tableView, 0, 5, 2, 1);

        Scene scene = new Scene(gridPane, 400, 300);
        primaryStage.setScene(scene);

        primaryStage.show();
    }

    // Currency Selection
    private double getExchangeRate(String currency) {
        switch (currency.split(" - ")[0]) {
            case "$USD":
                return 1;
            case "€EUR":
                return 0.846540;
            case "$AUD":
                return 1.354725;
            case "£GBP":
                return 0.733893;
            case "¥JPY":
                return 114.618000;
            case "$CAD":
                return 1.270743;
            case "$NZD":
                return 1.469310;
            case "₪ILS":
                return 3.239470;
            case "$HKD":
                return 7.765971;
            case "krNOK":
                return 8.810382;
            default:
                return 0.000;
        }
    }

    // Populate/Refresh Table
    private void populateTable(TableView<Conversion> tableView, String amountString, String selectedCurrency) {
        try {
            double amount = Double.parseDouble(amountString);
            double convertedAmount;
            int nextStep = (int) Math.ceil(amount);
            for (int i = 1; i <= nextStep; i *= 10) {
                if (i > amount) {
                    nextStep = i;
                    break;
                }
            }
            for (int i = 1; i <= nextStep; i *= 10) {
                convertedAmount = i * exchangeRate;
                tableView.getItems().add(new Conversion(String.valueOf(i), String.format("%.2f", convertedAmount)));
            }
        } catch (NumberFormatException ex) {
            // Handle exception
        }
    }

    // Method to update the conversion label
    private void updateConversionLabel(String amountString, String selectedCurrency, Label conversionLabel) {
        try {
            double amount = Double.parseDouble(amountString);
            double convertedAmount = amount * exchangeRate;
            conversionLabel.setText("Converted Amount: " + String.format("%.2f", convertedAmount) + " " + selectedCurrency.split(" - ")[0].substring(1));
        } catch (NumberFormatException ex) {
            // Handle exception
            conversionLabel.setText("");
        }
    }

    public static void main(String[] args) {
        launch(args);
    }

    public static class Conversion {
        private final SimpleStringProperty amount;
        private final SimpleStringProperty convertedAmount;

        public Conversion(String amount, String convertedAmount) {
            this.amount = new SimpleStringProperty(amount);
            this.convertedAmount = new SimpleStringProperty(convertedAmount);
        }

        public String getAmount() {
            return amount.get();
        }

        public String getConvertedAmount() {
            return convertedAmount.get();
        }
    }
}
