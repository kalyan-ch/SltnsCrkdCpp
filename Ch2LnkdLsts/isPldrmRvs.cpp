#include <iostream>
#include "LinkedList.h"
using namespace std;

Node* getReverse(Node* node, LinkedList* llRev){

	if(node->next == NULL){
		return node;
	}
	Node* n = getReverse(node->next, llRev);
	llRev->addNode(n->data);

	return node;

}

bool isPlnDrm(Node* head){
	bool flag = false;

	//get reverse of list
	LinkedList* llRev = new LinkedList();
	getReverse(head, llRev);
    llRev->addNode(head->data);
	llRev -> printList();
	//verify if same as original

	return flag;
}

int main(){

	LinkedList* ll1 = new LinkedList();
	LinkedList* ll2 = new LinkedList();

	//a palindrome
	ll1->addNode(7);
	ll1->addNode(8);
	ll1->addNode(3);
	ll1->addNode(9);
	ll1->addNode(3);
	ll1->addNode(8);
	ll1->addNode(7);

	//not a plndrm
	ll2->addNode(3);
	ll2->addNode(0);
	ll2->addNode(7);
	ll2->addNode(5);


	cout << "is list 1 a palindrome? " << isPlnDrm(ll1->head);
	//cout << "is list 2 a palindrome? " << isPlnDrm(ll2->head);

	return 0;
}
