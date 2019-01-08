class Solution {
    public boolean isUnivalTree(TreeNode root) {
		Stack<TreeNode> cacheTreeNode = new Stack();
		int data = root.val;
		cacheTreeNode.push(root);
		while(!cacheTreeNode.empty()){
			TreeNode tempNode = cacheTreeNode.pop();
			if(data != tempNode.val){
				return false;
			}
			else{
				if(tempNode.left != null){
					cacheTreeNode.push(tempNode.left);
				}
				if(tempNode.right != null){
					cacheTreeNode.push(tempNode.right);
				}
			}
		}
		return true;
    }
}
