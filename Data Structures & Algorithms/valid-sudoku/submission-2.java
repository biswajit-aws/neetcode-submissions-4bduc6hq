class Solution {
        public boolean isValidSudoku(char[][] board) {
        int col=board.length;
        Map<Integer,List<String>> map=new HashMap<>();
        Map<Integer,List<String>> iArray=new HashMap<>();
        Map<Integer,List<String>> jArray=new HashMap<>(); 
        for(int i=0;i<9;i++){
            for(int j=0;j<9;j++){
                if(board[i][j]!='.'){
                    int idx=((i/3)*3)+(j/3);
                    System.out.println("idx ="+idx+" "+i+" "+j);
                    String val=String.valueOf(board[i][j]);
                    List<String> square= map.getOrDefault(idx,new ArrayList<>());
                    List<String> row= iArray.getOrDefault(i,new ArrayList<>());
                    List<String> column= jArray.getOrDefault(j,new ArrayList<>());
                    if(square.contains(val)|| row.contains(val) || column.contains(val)){
                        return false;
                    }else{
                        square.add(val);
                        map.put(idx,square);
                         row.add(val);
                        iArray.put(i,row);
                         column.add(val);
                        jArray.put(j,column);
                        System.out.println("row"+iArray);
                         System.out.println("column"+jArray);
                          System.out.println("square"+map);
                    }

                }
            }

        }
                return true;

    }
}
