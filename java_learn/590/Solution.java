/*
// Definition for a Node.
class Node {
    public int val;
    public List<Node> children;

    public Node() {}

    public Node(int _val,List<Node> _children) {
        val = _val;
        children = _children;
    }
};
*/
class Solution {
	List<Integer> res = new ArrayList<Integer>();
	public void postOrderAssist(Node root){
		if(root != null){
			if(root.children != null){
				for(Node tempNode: root.children){
					postOrderAssist(tempNode);
				}
			}
			res.add(root.val);
		}
	}
    public List<Integer> postorder(Node root) {
		postOrderAssist(root);
		return res;
    }
}
