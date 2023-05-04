public class JCrash
{
    public static void main(String[] args)
    {
        final String message = null;
        System.out.printf("Here's the message: %s\n", message);
        System.out.printf("Here's the length of the message: %d\n", message.length());
    }
}
