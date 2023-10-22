public class Main {
    public static void main(String[] args) {
        int ease = 4; //this is going to be the rating that the user gives the card (1-5 stars depending on the ease, 1 being impossible and 5 being super easy)
        int repetition = 4; //each card is going to have a number to keep track of the repetition
        int interval = 3600; //the interval (in seconds) between each population of the specific card


        if (ease >= 3 && repetition > 1) {
            interval = (int)((interval * (EaseFactor(ease, previousIntervalCalculator(interval, ease, repetition))))+1);
            System.out.println(interval);
            System.out.println(repetition);
            System.out.println(ease);
        } else if (ease >= 3 && repetition < 1) {
            interval = (int)((EaseFactor(ease, previousIntervalCalculator(interval, ease, repetition))));
            System.out.println(interval);
            System.out.println(repetition);
            System.out.println(ease);
        } else {
            repetition = 0;
            interval = 60;
            System.out.println(interval);
            System.out.println(repetition);
            System.out.println(ease);
        }
    }

   // public static int create a method from the body, just name it and return the interval
    //create a method that creates the array that sorts and stores the interval from smallest to largest and returns that
    public static double EaseFactor (int ease, int previousInterval){
        double easeFactor = 0.0;
        easeFactor = previousInterval + (0.1 - (5 - ease) * (0.08 + (5 - ease) * 0.02));
        return easeFactor;
    }

    public static int previousIntervalCalculator(int interval, int ease, int repetition) {
        if (repetition < 1) {
            switch (ease) {
                case 5:
                    interval = 60;
                    break;
                case 4:
                    interval = 360;
                    break;
                case 3:
                    interval = 900;
                    break;
                case 2:
                    interval = 3600;
                    break;
                case 1:
                    interval = 43200;
                    break;
                default:
                    System.out.println("Error with grading, please select a diffculty out of 5");
                    break;
            }
        } else if (repetition > 0 && repetition < 1) {
            switch (ease) {
                case 5:
                    interval = 60;
                    break;
                case 4:
                    interval = 360;
                    break;
                case 3:
                    interval = 1800;
                    break;
                case 2:
                    interval = 43200;
                    break;
                case 1:
                    interval = 86400;
                    break;
                default:
                    System.out.println("Error with grading, please select a diffculty out of 5");
                    break;
            }
        } else {
            switch (ease) {
                case 5:
                    interval = 60;
                    break;
                case 4:
                    interval = 360;
                    break;
                case 3:
                    interval = 1800;
                    break;
                case 2:
                    interval = 86400;
                    break;
                case 1:
                    interval = 345600;
                    break;
                default:
                    System.out.println("Error with grading, please select a diffculty out of 5");
                    break;
            }
        }
        return interval;
    }
}