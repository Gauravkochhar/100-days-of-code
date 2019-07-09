class TreeNode{
    int info;
    TreeNode left;
    TreeNode right;
    
    TreeNode(int info){
        this.info = info;
        left = right = null;
    }
}

class MyBinaryTree{
    TreeNode root;
    
    MyBinaryTree(TreeNode root){
        this.root = root;
    }
    
    public void visit(TreeNode node){
        System.out.print(node.info+" -> ");
    }
    
    public void preOrder(TreeNode root){
        if(root == null){
            return;
        }
        visit(root);
        preOrder(root.left);
        preOrder(root.right);
    }
    
    public void postOrder(TreeNode root){
        if(root == null){
            return;
        }
        postOrder(root.left);
        postOrder(root.right);
        visit(root);
    }
    
    public void inOrder(TreeNode root){
        if(root == null){
            return;
        }
        postOrder(root.left);
        visit(root);
        postOrder(root.right);
    }
}

public class Main{
	public static void main(String[] args) {
	    TreeNode n6 = new TreeNode(6);
	    TreeNode n7 = new TreeNode(7);
	    TreeNode n9 = new TreeNode(9);
	    TreeNode n5 = new TreeNode(5);
	    TreeNode n2 = new TreeNode(2);
	    TreeNode n1 = new TreeNode(1);
	    
	    n6.left = n7;
	    n6.right = n9;
	    
	    n7.left = n5;
	    n7.right= n2;
	    
	    n9.left = n1;
	    
		MyBinaryTree mbt = new MyBinaryTree(n6);
	    System.out.println("PreOrder Of Tree is:");
	    mbt.preOrder(n6);
	    System.out.println("\n\nPostOrder Of Tree is:");
	    mbt.postOrder(n6);
	    System.out.println("\n\nInOrder Of Tree is:");
	    mbt.inOrder(n6);
	}
}
