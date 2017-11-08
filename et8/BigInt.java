import java.util.*;
import java.io.*;

public class BigInt{
  
  public static int GCD(int a, int b) { return b==0 ? a : GCD(b, a%b); }
  
  public static String rmZro(String st){
    int id =0;
    while(id < st.length()){
      if (st.charAt(id)=='0'){
        id++;
      }else{
        return st.substring(id);
      }
    }
    return "0";
  }
  
  public static String GCDBI(String a, String b){
    if(a.charAt(0) == '-'){
      a = a.substring(1);
    }
    if(b.charAt(0) == '-'){
      b = b.substring(1);
    }
    String tmp ="";
    String rsl ="";
    while(!a.equals("0") && !b.equals("0")){
      //System.out.println(!a.equals("0") || !b.equals("0"));
      tmp = b;
      rsl = divBI(a, b);
      b = rsl.substring(rsl.indexOf(" ")+1);
      a = tmp;
    }
    return addBI(a,b);
  }
  
  public static String divBI(String f, String s){
    if(f.charAt(0) == '-' && s.charAt(0) == '-'){
      f = f.substring(1);
      s = s.substring(1);
    }else if(f.charAt(0) == '-'){
      return "-"+divBI(f.substring(1), s);
    }else if(s.charAt(0) == '-'){
      return "-"+divBI(f, s.substring(1));
    }
    int i = 0;
    while(greaterT(f,s).equals("true")||f.equals(s)){
      //System.err.println(i);
      f = minBI(f, s);
      i++;
    }
    return i + " " + f;
  }
  
  public static String mulBI(String f, String s){
    if(f.charAt(0) == '-' && s.charAt(0) == '-'){
      f = f.substring(1);
      s = s.substring(1);
    }else if(f.charAt(0) == '-'){
      return "-"+mulBI(f.substring(1), s);
    }else if(s.charAt(0) == '-'){
      return "-"+mulBI(f, s.substring(1));
    }
    ArrayList<String> rsl = new ArrayList<String>();
    String rtn ="";
    int tmp = 0;
    int rmd = 0;
    String zro = "";
    f = new StringBuilder(f).reverse().toString();
    s = new StringBuilder(s).reverse().toString();
    for(int i = 0; i < f.length(); i++){
      rtn = zro;
      rmd = 0;
      for(int j = 0; j<s.length();j++){
        tmp = Integer.parseInt(f.substring(i, i+1))*Integer.parseInt(s.substring(j, j+1))+rmd;
        rtn += String.valueOf(tmp%10);
        rmd = tmp/10;
      }
      rtn += rmd;
      rsl.add(rmZro(new StringBuilder(rtn+zro).reverse().toString()));
      zro +="0";
    }
    rtn = rsl.get(0);
    for(int i = 1; i<rsl.size(); i++){
      rtn = addBI(rtn, rsl.get(i));
    }
    return rtn;
  }
  
  public static String minBI(String f, String s){
    boolean n = false;
    if(f.charAt(0) == '-' && s.charAt(0) == '-'){
      f = f.substring(1);
      s = s.substring(1);
      n = !n;
    }else if(f.charAt(0) == '-'){
      return "-"+addBI(f.substring(1), s);
    }else if(s.charAt(0) == '-'){
      return addBI(f, s.substring(1));
    }
    int rmd = 0;
    String rtn = "";
    int tmp = 0;
    if(lessT(f,s).equals("true")){
      rtn = s;
      s = f;
      f = rtn;
      n = !n;
    }
    f = new StringBuilder(f).reverse().toString();
    s = new StringBuilder(s).reverse().toString();
    rtn = "";
    for(int i = 0; i < f.length(); i++){
      if(i < s.length()){
        tmp = Integer.parseInt(s.substring(i,i+1));
      }else{
        tmp = 0;
      }
      if((Integer.parseInt(f.substring(i,i+1))-rmd)< tmp){
        rtn += ""+(10+Integer.parseInt(f.substring(i,i+1))-rmd-tmp);
        rmd = 1;
      }else{
        rtn += Integer.parseInt(f.substring(i,i+1))-rmd-tmp;
        rmd = 0;
      }
    }
    rtn = new StringBuilder(rtn).reverse().toString();
    rtn = rmZro(rtn);
    rtn = (n? "-" : "")+rtn;
    return rtn;
  }
  
  public static String addBI(String f, String s){
    boolean n = false;
    if(f.charAt(0) == '-' && s.charAt(0) == '-'){
      f = f.substring(1);
      s = s.substring(1);
      n = !n;
    }else if(f.charAt(0) == '-'){
      f = minBI(f.substring(1), s);
      return (f.charAt(0)=='-')? f.substring(1) : "-"+f;
    }else if(s.charAt(0) == '-'){
      return minBI(f, s.substring(1));
    }
    int rmd = 0;
    String rtn = "";
    int tmp = 0;
    f = new StringBuilder(f).reverse().toString();
    s = new StringBuilder(s).reverse().toString();
    if(s.length() > f.length()){
      rtn = s;
      s = f;
      f = rtn;
    }
    rtn = "";
    for(int i = 0; i < f.length(); i++){
      if(i < s.length()){
        rmd += Integer.parseInt(s.substring(i,i+1));
      }
      tmp = Integer.parseInt(f.substring(i,i+1))+rmd;
      rtn += ""+tmp%10;
      rmd = tmp/10;
    }
    rtn = new StringBuilder(rtn).reverse().toString();
    return (n? "-" : "")+rmZro(rtn);
  }
  
  //i know i can just inverse this, but copypasta is much easier ;)
  public static String lessT(String fns, String sns){
    if(fns.charAt(0) == '-' && sns.charAt(0) == '-'){
      fns = fns.substring(1);
      sns = sns.substring(1);
    }else if(fns.charAt(0) == '-'){
      return "true";
    }else if(sns.charAt(0) == '-'){
      return "false";
    }
    if(fns.length() == sns.length()){
      for(int i = 0; i<fns.length(); i++){
        if(Integer.valueOf(fns.substring(i,i+1))<Integer.valueOf(sns.substring(i,i+1))){
          return ("true");
        }else if(Integer.valueOf(fns.substring(i,i+1))>Integer.valueOf(sns.substring(i,i+1))){
          return ("false");
        }
      }
      return ("false");
    }
    return (""+(fns.length() < sns.length()));
  }
  
  public static String greaterT(String fns, String sns){
    if(fns.charAt(0) == '-' && sns.charAt(0) == '-'){
      fns = fns.substring(1);
      sns = sns.substring(1);
    }else if(fns.charAt(0) == '-'){
      return "false";
    }else if(sns.charAt(0) == '-'){
      return "true";
    }
    if(fns.length() == sns.length()){
      for(int i = 0; i<fns.length(); i++){
        if(Integer.valueOf(fns.substring(i,i+1))>Integer.valueOf(sns.substring(i,i+1))){
          return ("true");
        }else if(Integer.valueOf(fns.substring(i,i+1))<Integer.valueOf(sns.substring(i,i+1))){
          return ("false");
        }
      }
      return ("false");
    }
    return (""+(fns.length() > sns.length()));
  }
  
  public static String operator(int fn, String op, int sn){
    String re = "# ";
    switch(op){
      case "+": return re + String.valueOf(fn+sn);
      case "-": return re + String.valueOf(fn-sn);
      case "*": return re + mulBI(String.valueOf(fn),String.valueOf(sn));
      case "/": return re + String.valueOf(fn/sn) + " " + fn%sn;
      case "<": return re + String.valueOf(fn<sn);
      case ">": return re + String.valueOf(fn>sn);
      case "=": return re + String.valueOf(fn==sn);
      case "gcd": return re + String.valueOf(GCD(fn, sn));
    }
    return "# Syntax error";
  }
  public static void main(String[] args){
    String str = "";
    String ostr = "";
    String op ="";
    String fns ="";
    String sns ="";
    int fn = 0;
    int sn = 0;
    Scanner sc = new Scanner(System.in);
    while( sc.hasNextLine() ){
      ostr = sc.nextLine();
      str = ostr;
      if(str.length()!=0){
        if(str.charAt(0)!='#'){
          try{
            fn = Integer.valueOf(str.substring(0, str.indexOf(' ')));
            str = str.substring(str.indexOf(' ')+1);
            op = str.substring(0, str.indexOf(' '));
            str = str.substring(str.indexOf(' ')+1);
            sn = Integer.valueOf(str);
            System.out.println(operator(fn,op,sn));
          }catch(NumberFormatException e){
            try{
              str = ostr;
              fns = rmZro(str.substring(0, str.indexOf(' ')));
              str = str.substring(str.indexOf(' ')+1);
              op = str.substring(0, str.indexOf(' '));
              str = str.substring(str.indexOf(' ')+1);
              sns = rmZro(str);
              str = str.substring(str.indexOf(' ')+1);
              System.out.print("# ");
              switch(op){
                case "=": 
                  System.out.println(fns.equals(sns));
                  break;
                case "<":
                  System.out.println(lessT(fns,sns));
                  break;
                case ">":
                  System.out.println(greaterT(fns,sns));
                  break;
                case "+":
                  System.out.println(addBI(fns,sns));
                  break;
                case "-":
                  System.out.println(minBI(fns,sns));
                  break;
                case "*":
                  System.out.println(mulBI(fns,sns));
                  break;
                case "/":
                  System.out.println(divBI(fns,sns));
                  break;
                case "gcd":
                  System.out.println(GCDBI(fns,sns));
                  break;
              }
            }catch(NumberFormatException hg){
              System.out.println("Syntax error");
            }
          }catch(Throwable e){
            System.out.println("# Syntax error");
          }
        }
      }
    }
  }
}