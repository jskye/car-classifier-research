/**
 * Created by Julius Myszkowski on 2/05/2015.
 * Subject: ${subjectCode} - ${subjectTitle}
 * University of Newcastle
 * Student Number: c3155112
 * email: c3155112@uon.edu.au, julius.skye@gmail.com
 */
import javax.imageio.ImageIO;
import javax.swing.*;
import java.awt.*;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;
import java.util.List;



public class FeatureRecogniserResultView {

    private List<Rectangle> detectionRectangles;
    String imgName;


    public FeatureRecogniserResultView(String imageName, List<Rectangle> res) {

        detectionRectangles = res;
        imgName = imageName;

        EventQueue.invokeLater(new Runnable() {
            @Override
            public void run() {
                try {
                    UIManager.setLookAndFeel(UIManager.getSystemLookAndFeelClassName());
                } catch (ClassNotFoundException | InstantiationException | IllegalAccessException | UnsupportedLookAndFeelException ex) {
                }
                JFrame frame = new JFrame("Testing");
                frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
                frame.setLayout(new BorderLayout());
                frame.add(new TestPane());
                frame.pack();
                frame.setLocationRelativeTo(null);
                frame.setVisible(true);
            }
        });
    }

    public class TestPane extends JPanel {

        private BufferedImage detectorImage;



        public TestPane() {
            try {
                detectorImage = ImageIO.read(new File(imgName));
            } catch (IOException ex) {
                ex.printStackTrace();
            }
        }

        @Override
        public Dimension getPreferredSize() {
            return detectorImage == null ? new Dimension(200, 200) : new Dimension(detectorImage.getWidth(), detectorImage.getHeight());
        }

        @Override
        protected void paintComponent(Graphics g) {
            super.paintComponent(g);
            Graphics2D g2d = (Graphics2D) g.create();
            if (detectorImage != null) {

                int x = (getWidth() - detectorImage.getWidth()) / 2;
                int y = (getHeight() - detectorImage.getHeight()) / 2;
                g2d.drawImage(detectorImage, x, y, this);

                g2d.setColor(Color.RED);
                g2d.translate(x, y);
                if(!detectionRectangles.isEmpty()) {

                    for(int i=0; i < detectionRectangles.size(); i++) {
                        g2d.draw(detectionRectangles.get(i));
                    }
                }
                else{
                    System.out.println("No such objects found in this image");
                }

            }

            g2d.dispose();
        }
    }

}