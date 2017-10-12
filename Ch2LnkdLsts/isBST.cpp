/* Hidden stub code will pass a root argument to the function below. Complete the function to solve the challenge. Hint: you may want to write one or more helper functions.  

The Node struct is defined as follows:
   struct Node {
      int data;
      Node* left;
      Node* right;
   }
*/
    
vector<int> arr;

bool isSorted(){
    
    for (int i = 0; i < arr.size(); i++){
        if(i != (arr.size() - 1) ){
            if(arr[i]>arr[i+1]){
                return false;
            }
        }
    }

    return true;
}

void appendInOrd(Node* ele){
	if(ele!=NULL){
		appendInOrd(ele->left);
	    arr.push_back(ele->data);
	    appendInOrd(ele->right);
	}
	
    
}

bool checkBST(Node* root) {

	if(root == NULL){
		return false;
	}

	appendInOrd(root);

	if(arr.size() == 1 or isSorted()){
		return true;
	}
  
}
