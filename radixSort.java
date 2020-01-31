import java.util.*;
class Buckets {
    public List<String> zeroBucket;
    public List<String> oneBucket;
    public Buckets() {
        zeroBucket = new ArrayList<>();
        oneBucket = new ArrayList<>();
    }
    public void addZero(String newValue) {
        zeroBucket.add(newValue);
    }
    public void addOne(String newValue) {
        oneBucket.add(newValue);
    }
    public List<String> getAllInOrder() {
        List<String> result = new ArrayList<>();
        for (String val: oneBucket) {
            result.add(val);
        }
        for (String val: zeroBucket) {
            result.add(val);
        }
        return result;
    }
}

public class radixSort extends Buckets{

    public List<String> partialSort(List<String> list, int x){ //sort given list by digit at digit position, return new sorted list
        int size = list.size();
        //System.out.println(list);

        Buckets buckets = new Buckets();
            for (int j = 0; j< size; j++){
                String element = list.get(j);
                //System.out.println(element);
                if (element.charAt(x)=='0'){
                    buckets.addZero(element);}
                else {buckets.addOne(element);}
                }
        //System.out.println(buckets.oneBucket);

        List<String> newlist = buckets.getAllInOrder();
            //System.out.println(buckets.getAllInOrder());

            return buckets.getAllInOrder();
            }

    public List<String> radixSort(List<String> list, int numDigits){ //implements radixSort by calling partialSort for each digit position starting at last position, returns sorted list
        for (int i = numDigits-1; i>=0; i--){
            list = partialSort(list, i);
            System.out.println(i+1 +"th digit "+list);
        }
        return list;
    }


    public static void main (String[] args){
        String[] origNumbers = {"0011", "1001", "1000", "0111", "0101"};
        List<String> numbers = new ArrayList<>();
        for (String num: origNumbers) {
            numbers.add(num);
        }
        int numDigits = 4;
        radixSort sort = new radixSort();
        List<String> sortedList;
        System.out.println("start: "+numbers);
        sortedList = sort.radixSort(numbers, numDigits);
        System.out.println("result: "+sortedList);

    }
}
