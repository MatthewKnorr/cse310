import javafx.application.Application;
import javafx.geometry.Insets;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.layout.GridPane;
import javafx.stage.Stage;

public class Main extends Application {

    @Override
    public void start(Stage primaryStage) {
        // Create a grid pane layout
        GridPane gridPane = new GridPane();
        gridPane.setPadding(new Insets(10));
        gridPane.setHgap(5);
        gridPane.setVgap(5);

        // Create buttons
        Button button1 = new Button("1");
        Button buttonPlus = new Button("+");
        Button button2 = new Button("2");

        // Add buttons to the grid pane
        gridPane.add(button1, 0, 0);
        gridPane.add(buttonPlus, 1, 0);
        gridPane.add(button2, 2, 0);

        // Create scene and set the grid pane as the root
        Scene scene = new Scene(gridPane, 200, 100);

        // Set the stage title and scene, then show the stage
        primaryStage.setTitle("Simple Calculator");
        primaryStage.setScene(scene);
        primaryStage.show();
    }

    public static void main(String[] args) {
        launch(args);
    }
}
