class Solution{
	public int[][] flipAndInvertImage(int[][] A){
		int[][] flipA = flipImage(A);
		int[][] flipInvertA = invertImage(flipA);
		return flipInvertA;
	}
	public int[][] flipImage(int[][] A){
		int length = A[0].length;
		for(int i=0; i<A.length; i++){
			for(int j=0; j<length/2; j++){
				int temp = A[i][j];
				A[i][j] = A[i][length-1-j];
				A[i][length-1-j] = temp;
			}
		}
		return A;
	}
	public int[][] invertImage(int[][] A){
		for(int i=0; i<A.length; i++){
			for(int j=0; j<A[0].length; j++){
				int temp = A[i][j];
				A[i][j] = 1 - temp;
			}
		}
		return A;
	}
}
