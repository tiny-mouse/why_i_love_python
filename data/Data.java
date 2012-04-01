import java.util.HashMap;
import java.util.Map;

public class Data {
    public static void main(String[] args) {
        /**
         * You all know this stuff
         * Java Types and Primitives: 
         * null
         * true/false
         * char -> String
         * int -> Integer
         */
    	Object o = null;
    	System.out.println(o);
    	o = new String("Hi, Java");
    	System.out.println(o);
    	
    	//Because Java is type safe, specify what the types
    	Map<String, String> dict = new HashMap<String, String>();
    	dict.put("key1", "arg1");
    	dict.put("key2", "arg2");
    	dict.put("key3", "arg3");
    	
    	// You can also say Object, Object, but that is far less elegant
    	// java-ers may want to hurt you if you do this
    	Map<Object, Object> objectDict = new HashMap<Object, Object>();
    	//objectDict.put("anumber", new Integer(1));
    	//Integer anInt = (String)objectDict.get("anumber");
    	objectDict.put("dict", dict);
    	objectDict.put(dict, objectDict);
    	
    	//String!
    	String s = "hi!";
    	
    	//int
    	int anInt = 42;
    	
    	//double
    	double aDouble = 10.002736393;
    	
    	boolean thisIsAlwaysFalse = true;
    }
}
