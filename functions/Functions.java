public class Functions {
    public static void doSomething() {
        System.out.println("I did something!");
    }

    public static int add(int a, int b) {
        return a+b;
    }

    public static void main(String[] args) {
        Functions.doSomething();
        try {
            if (args[0].equals("add") && args.length == 3) {
                System.out.println(Functions.add(Integer.parseInt(args[1]), Integer.parseInt(args[2])));
            }
        } catch (IllegalArgumentException e) {
            System.out.println("One of your args is not an int.  usage: operation, number 1, number 2");
        }
    }
}
