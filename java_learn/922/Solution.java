class Solution{
	public int[] sortArrayByParityII(int[] A){
		int[] arrEven = new int[A.length / 2];
		int[] arrOdd = new int[A.length / 2];
		int[] arrRes = new int[A.length];
		int indexEven = 0;
		int indexOdd = 0;
		for(int i:A){
			if(i % 2 == 0){
				arrEven[indexEven] = i;
				indexEven += 1;
			}
			else{
				arrOdd[indexOdd] = i;
				indexOdd += 1;
			}
		}
		for(int i=0; i<indexOdd; i++){
			arrRes[2*i] = arrEven[i];
			arrRes[2*i+1] = arrOdd[i];
		}
		return arrRes;
	}
}
