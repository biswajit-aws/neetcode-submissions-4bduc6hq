class MinStack {
    List<Integer> stack=null;
    int top=-1;


    public MinStack() {
        stack=new ArrayList<>();
    }
    
    public void push(int val) {
            stack.add(val);
            top=top+1;
    }
    
    public void pop() {
        if(!stack.isEmpty()){
        stack.remove(top);
        top=top-1;
        }else{
            throw new RuntimeException("");
        }
    }
    
    public int top() {
        return stack.get(top);
    }
    
    public int getMin() {
       if(!stack.isEmpty()){
        int min=Integer.MAX_VALUE;
          for(int i:stack){
            min=Math.min(i,min);
          }
          return min;
        }else{
            throw new RuntimeException("");
        }
    }
}
