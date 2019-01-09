class Solution{
	public boolean judgeCircle(String moves){
		int valueHor = 0;
		int valueVer = 0;
		char[] cacheAction = moves.toCharArray();
		for(char tempAction : cacheAction){
			if(tempAction == 'U'){
				valueVer += 1;
			}
			else if(tempAction == 'D'){
				valueVer -= 1;
			}
			else if(tempAction == 'R'){
				valueHor += 1;
			}
			else{
				valueHor -= 1;
			}
		}
		if(valueHor == 0 && valueVer == 0){
			return true;
		}
		else{
			return false;
		}
	}
}
