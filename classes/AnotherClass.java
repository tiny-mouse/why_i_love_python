public class AnotherClass extends AClass {

    public AnotherClass() {
         // I am a Java comment.
    }

    public void someOtherMethod() {
        System.out.println("My attribute is: " + this.attribute);
    }

    public static void main(String[] args) {
        AnotherClass aClass = new AnotherClass();
        aClass.someOtherMethod();
    }
}
