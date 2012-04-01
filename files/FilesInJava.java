import java.io.BufferedWriter;
import java.io.IOException;
import java.nio.charset.Charset;
import java.nio.file.Files;
import java.nio.file.Path;



public class FilesInJava {
    public static void main(String[] args) {
        Charset charset = Charset.forName("US-ASCII");
        String s = "I am a new file from Java";
        try {
            // OMFG why is it so hard to open a file?!?!?
            Path path = FileSystems.getDefault().getPath(".", "new_file_from_java.txt");
            BufferedWriter writer = Files.newBufferedWriter(path, charset);
            writer.write(s, 0, s.length());
        } catch (IOException x) {
            System.err.format("IOException: %s%n", x);
        }
        
    }
}
