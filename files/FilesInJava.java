import java.io.*;


public class FilesInJava {
    public static void main(String[] args) {
        String s = "I am a new file from Java";
        try {
            // OMFG why is it so hard to write a friggin file?!!?
            BufferedWriter writer = new BufferedWriter(new FileWriter("new_file_from_java.txt"));
            writer.write(s);
            writer.close();
        } catch (IOException x) {
            System.err.format("IOException: %s%n", x);
        }
        
    }
}
