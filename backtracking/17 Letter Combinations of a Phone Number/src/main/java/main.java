package Main;

class Main{
    public static void main (String[] args){
        String input= new String("23");
        Solution call = new Solution();
        for(String x:call.letterCombinations(input)){
            System.out.print(x+" ");
        }
        System.out.println();
        for(String x:call.letterCombinations("234")){
            System.out.print(x+" ");
        }
    }

}