import detection.Detector;
import java.awt.*;
import java.util.List;


class ViolaJonesDetection {

    public static void main(String[] args) {

        String fileName="freeway_cars_infront.jpg";
        Detector detector=Detector.create("lvt.xml");
        List<Rectangle> res=detector.getFaces(fileName, 1.2f, 1.1f, .05f, 2, true);
        //System.out.print(res.toString());
        new FeatureRecogniserResultView(fileName, res);
    }



    }
