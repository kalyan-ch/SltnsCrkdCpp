
#include <iostream>
#include "LinkedList.h"

using namespace std;

Node* kthEle(Node* head, int k){
	Node* p1 = head;
	Node* p2 = head;

	for (int i = 0; i < k; ++i){
		if(p1==NULL){
			return NULL;
		}
		p1 = p1->next;
	}
	cout << p1 -> data << endl;
	while(p1!=NULL){
		p1 = p1->next;
		p2 = p2->next;
	}

	return p2;


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

	Node* ele = kthEle(ll->head, 3);
	cout << ele->data;

	return 0;
}
