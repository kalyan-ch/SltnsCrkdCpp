#include <iostream>
#include <vector>
#include "LinkedList.h"

using namespace std;

Node* reverseList(Node* head, int k){
	
	Node* n = head;
	Node* n1;
	
	//get last node in group
	
	int i = 1;
	while (i<k){
		Node* n1 = n;
		Node* n2 = n->next;
		//swap
		n = n->next;
	    n1->next = n2->next;
	    n->next = n1;

	    //go to next
	    n = n->next;
	    i++;
	}
    
	head = n;
	Node* temp2 = head->next;
	head->next = temp;
	n1->next = temp2;
	
	return head;

}

int main(){
	LinkedList* ll1 = new LinkedList();

	ll1->addNode(7);
	ll1->addNode(2);
	ll1->addNode(8);
	ll1->addNode(1);
	
	ll1->printList();
	ll1->head = reverseList(ll1->head,3);
	ll1->printList();

	return 0;
}
