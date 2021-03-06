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
	bool flag = true;

	//get reverse of list
	LinkedList* llRev = new LinkedList();
	getReverse(head, llRev);
    llRev->addNode(head->data);
	
	//verify if same as original
	Node* n = head;
	Node* n1 = llRev->head; 
    
    while(n!=NULL && n1!=NULL){
    	if(n->data!=n1->data){
    		flag = false;
    	}
    	n = n->next;
    	n1 = n1->next;
    }

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
