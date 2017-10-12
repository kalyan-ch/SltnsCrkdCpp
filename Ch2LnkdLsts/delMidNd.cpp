

#include <iostream>
#include "LinkedList.h"

using namespace std;

void deleteMidNode(Node* n){
	if(n==NULL || n->next==NULL ){
		return;
	}
	Node* a = n->next;
	n->data = a->data;
	n->next = a->next;

}

int main(){

	LinkedList* ll = new LinkedList();
	ll->addNode(20);
	ll->addNode(10);
	ll->addNode(30);
	ll->addNode(30);
	ll->addNode(30);
	Node* n = ll->addNode(20);
	ll->addNode(15);
	ll->addNode(30);
	deleteMidNode(n);
	return 0;
}
