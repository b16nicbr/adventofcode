import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

public class Main {
    public static void main(String[] args) {


        Stack<String> list1 = new Stack<>();
        Stack<String> list2 = new Stack<>();
        Stack<String> list3 = new Stack<>();
        Stack<String> list4 = new Stack<>();
        Stack<String> list5 = new Stack<>();
        Stack<String> list6 = new Stack<>();
        Stack<String> list7 = new Stack<>();
        Stack<String> list8 = new Stack<>();
        Stack<String> list9 = new Stack<>();

        list1.push("S");
        list1.push("L");
        list1.push("W");

        list2.push("J");
        list2.push("T");
        list2.push("N");
        list2.push("Q");

        list3.push("S");
        list3.push("C");
        list3.push("H");
        list3.push("F");
        list3.push("J");


        list4.push("T");
        list4.push("R");
        list4.push("M");
        list4.push("W");
        list4.push("N");
        list4.push("G");
        list4.push("B");

        list5.push("T");
        list5.push("R");
        list5.push("L");
        list5.push("S");
        list5.push("D");
        list5.push("H");
        list5.push("Q");
        list5.push("B");

        list6.push("M");
        list6.push("J");
        list6.push("B");
        list6.push("V");
        list6.push("F");
        list6.push("H");
        list6.push("R");
        list6.push("L");

        list7.push("D");
        list7.push("W");
        list7.push("R");
        list7.push("N");
        list7.push("J");
        list7.push("M");

        list8.push("B");
        list8.push("Z");
        list8.push("T");
        list8.push("F");
        list8.push("H");
        list8.push("N");
        list8.push("D");
        list8.push("J");

        list9.push("H");
        list9.push("L");
        list9.push("Q");
        list9.push("N");
        list9.push("B");
        list9.push("F");
        list9.push("T");
        System.out.println("--------------------");
        System.out.println(list1);
        System.out.println(list2);
        System.out.println(list3);
        System.out.println(list4);
        System.out.println(list5);
        System.out.println(list6);
        System.out.println(list7);
        System.out.println(list8);
        System.out.println(list9);
        System.out.println(list1.lastElement());
        list5.push(list4.lastElement());
        list4.pop();
        list5.push(list4.lastElement());
        list4.pop();
        list5.push(list4.lastElement());
        list4.pop();
        list5.push(list4.lastElement());
        list4.pop();
        list5.push(list4.lastElement());
        list4.pop();
        System.out.println("--------------------");
        System.out.println(list1);
        System.out.println(list2);
        System.out.println(list3);
        System.out.println(list4);
        System.out.println(list5);
        System.out.println(list6);
        System.out.println(list7);
        System.out.println(list8);
        System.out.println(list9);
        list8.push(list5.lastElement());
        list5.pop();
        list8.push(list5.lastElement());
        list5.pop();
        System.out.println("--------------------");
        System.out.println(list1);
        System.out.println(list2);
        System.out.println(list3);
        System.out.println(list4);
        System.out.println(list5);
        System.out.println(list6);
        System.out.println(list7);
        System.out.println(list8);
        System.out.println(list9);

    }



}