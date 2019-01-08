class Solution{
	public int numUniqueEmails(String[] emails){
		int res = 0;
		Map cacheEmailAddress = new HashMap();
		for(String tempEmail: emails){
			String[] tempEmailData = tempEmail.split("@");
			String localName = tempEmailData[0];
			String domainName = tempEmailData[1];
			int plusIndexLocalName = localName.indexOf(String.valueOf('+'));
			if(plusIndexLocalName >= 0){
				localName = localName.substring(0, plusIndexLocalName);
			}
			String[] localNameDot = localName.split("\\.");
			localName = "";
			for(String tempLocalNamePart: localNameDot){
				localName += tempLocalNamePart;
			}
			String emailAddress = localName + "@" + domainName;
			if(cacheEmailAddress.get(emailAddress) == null){
				res += 1;
				cacheEmailAddress.put(emailAddress, "1");
			}
		}
		return res;
	}
}
