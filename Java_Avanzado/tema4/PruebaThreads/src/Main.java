public class Main {
    public static void main(String[] args) {
        NoThread no = new NoThread();
        SiThread si = new SiThread();
        no.start();
        si.start();
//        for (int i=0; i<20; i++)
//            System.out.print("SI ");
    }
}

class NoThread extends Thread {
    public void run() {
        for (int i=0; i<2000; i++)
            System.out.print("NO ");
    }
}

class SiThread extends Thread {
    public void run() {
        for (int i=0; i<2000; i++)
            System.out.print("SI ");
    }
}
