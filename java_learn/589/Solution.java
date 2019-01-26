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
    public List<Integer> preorder(Node root) {
		Stack<Node> cacheNode = new Stack<Node>();
		List<Integer> res = new ArrayList<Integer>();
		cacheNode.push(root);
		while(cacheNode.size() > 0){
			Node tempNode = cacheNode.pop();
			if(tempNode == null){
				continue;
			}
			for(int i=tempNode.children.size()-1; i>=0; i--){
				cacheNode.push(tempNode.children.get(i));
			}
			res.add(tempNode.val);
		}
		return res;
    }
}
