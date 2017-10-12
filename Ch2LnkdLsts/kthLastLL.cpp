#include <iostream>
#include "LinkedList.h"

int kthEle(int k, Node* node){
	if(node == NULL){
		return 0;
	}

	int index = kthEle(k, node->next)+1;
	if(index == k){
		cout << "kth to the last element is: " << node->data << "\n";
	}

	return index;
}

int main(){
	LinkedList* ll = new LinkedList();
	ll->addNode(25);
	ll->addNode(12);
	ll->addNode(32);
	ll->addNode(35);
	ll->addNode(73);
	ll->addNode(27);
	ll->addNode(15);
	ll->addNode(42);
	ll->printList();

	kthEle(5,ll->head);

	return 0;
}


