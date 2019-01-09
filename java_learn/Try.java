public class Try{
	public static void main(String []args){
		String data = "abcdefg";
		String[] A = {"abc"};
		char[][] cacheChar = new char[A.length][(A[0]).length()];
		for(int i=0; i<A.length; i++){
			char[] tempChar = A[i].toCharArray();
			for(int j=0; j<A[0].length(); j++){
				cacheChar[i][j] = tempChar[j];
			}
		}
		System.out.println(cacheChar[0][2]);
	}
}
