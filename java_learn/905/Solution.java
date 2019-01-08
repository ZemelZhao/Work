class Solution{
	public int[] sortArrayByParity(int[] A){
		int[] res = new int[A.length];
		int index = 0;
		for(int a: A){
			if(a % 2 == 0){
				res[index] = a;
				index += 1;
			}
		}
		for(int a: A){
			if(a % 2 == 1){
				res[index] = a;
				index += 1;
			}
		}
		return res;
	}
}
