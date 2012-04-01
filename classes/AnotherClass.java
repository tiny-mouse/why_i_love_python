/**
 * Notice that the sub-class has to be in a separate file from the parent class.
 */
public class AnotherClass extends AClass {

    public AnotherClass() {
         // I am a Java comment.
    }

    public void someOtherMethod() {
        System.out.println("My attribute is: " + this.attribute);
    }

    /**
     * Oh hey der.  The main is IN the class???
     */
    public static void main(String[] args) {
        AnotherClass aClass = new AnotherClass();
        aClass.someMethod();
        aClass.someOtherMethod();
    }
}
