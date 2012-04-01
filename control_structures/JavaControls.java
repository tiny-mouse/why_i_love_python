import java.util.Arrays;
import java.util.Set;
import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;
import java.util.Random;

public class JavaControls {
    public static void ifStatement() {
        System.out.println("IF STATEMENT");
        Random random = new Random();
        int num = random.nextInt(10);
        System.out.println("The random we got is: "+num);
        if (num < 5) {
            System.out.println(num + "is less than 2");
        } else if (num > 1 && num < 6) {
            System.out.println(num + "is greater than 1 and less than 6");
        } else {
            System.out.println(num + " don't care.");
        }

    }

    public static void whileLoop() {
        System.out.println("WHILE STATEMENT");
        Random random = new Random();
        int num = random.nextInt(10);
        while (num > 0) {
            System.out.println("While loop num: "+num);
            num--;
        }
    }

    public static void forLoop() {
        for (int i = 0; i < 20; i++) {
            System.out.println("for loop iteration: "+i);
        }
    }

    public static void listIterator() {
        System.out.println("CAN'T REALLY DO LIST ITERATORS IN JAVA");
        int[] theList = new int[10];
        for (int i = 0; i < 10; i++) {
            theList[i] = i;
        }
        System.out.println(Arrays.toString(theList));
    }

    public static void forDictLoop() {
        System.out.println("DICT ITERATION");
        Map<Object,Integer> mp = new HashMap<Object, Integer>();

        // Notice they have to be of type Object, so you can't put int or char as the key.
        for (int i = 0; i < 10; i++) {
            mp.put(new Integer(i), new Integer(i+10));
        }
        Set s=mp.entrySet();

        Iterator it=s.iterator();

        while(it.hasNext())
        {
            Map.Entry m =(Map.Entry)it.next();

            int key=(Integer)m.getKey();

            Integer value=(Integer)m.getValue();

            // Notice you don't have to call toString explicitly on Objects that
            // implement it.  The print methods will do it for you.
            System.out.println("Key :"+key+"  Value :"+value);
        }
            
        
    }

    public static void main(String[] args) {
        JavaControls.ifStatement();
        JavaControls.whileLoop();
        JavaControls.forLoop();
        JavaControls.listIterator();
        JavaControls.forDictLoop();
    }
}
