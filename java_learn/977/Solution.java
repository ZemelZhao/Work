class Solution {
    public int[] sortedSquares(int[] A) {
		int indexPos = 0;
		int[] res = new int[A.length];
		for(int i=0; i<A.length; i++){
			if(A[i] >= 0){
				indexPos = i;
				break;
			}
		}
		Stack<Integer> cacheNegSquare = new Stack<Integer>();
		Stack<Integer> cachePosSquare = new Stack<Integer>();
		for(int i=0; i<indexPos; i++){
			cacheNegSquare.push(A[i]*A[i]);
		}
		for(int i=A.length-1; i>= indexPos; i--){
			cachePosSquare.push(A[i]*A[i]);
		}
		indexPos = 0;
		while(!(cachePosSquare.empty() | cacheNegSquare.empty())){
			if(cacheNegSquare.peek() > cachePosSquare.peek()){
				res[indexPos] = cachePosSquare.pop();
			}
			else{
				res[indexPos] = cacheNegSquare.pop();
			}
			indexPos += 1;
		}
		if(cachePosSquare.empty()){
			while(!cacheNegSquare.empty()){
				res[indexPos] = cacheNegSquare.pop();
				indexPos += 1;
			}
		}
		if(cacheNegSquare.empty()){
			while(!cachePosSquare.empty()){
				res[indexPos] = cachePosSquare.pop();
				indexPos += 1;
			}
		}
		return res;
    }
}
