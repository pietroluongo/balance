#ifndef WIFI_STUFF_H
#define WIFI_STUFF_H
#include <PubSubClient.h>

void reconnect(PubSubClient &client);
void setup_wifi(PubSubClient &client);

#endif