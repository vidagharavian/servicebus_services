from azure.servicebus import ServiceBusMessage
from azure.servicebus.aio import ServiceBusClient


class SBService:
    def __init__(self, conn_str: str, queue_name: str=None, subscription_name: str = None,topic_name=None):
        self.conn_str = conn_str
        self.queue_name = queue_name
        self.topic_name = topic_name
        self.subscription_name = subscription_name

    async def send_message(self, message_body: str, application_properties=None):
        if application_properties is None:
            application_properties = {}
        async with ServiceBusClient.from_connection_string(
                conn_str=self.conn_str,
                logging_enable=True) as servicebus_client:
            # Get a Queue Sender object to send messages to the queue
            self.sender = servicebus_client.get_queue_sender(queue_name=self.queue_name)
            message = ServiceBusMessage(message_body,application_properties=application_properties)
            await self.sender.send_messages(
                message
            )

    async def receive_from_subscription(self):
        # create a Service Bus client using the connection string
        async with ServiceBusClient.from_connection_string(
                conn_str=self.conn_str,
                logging_enable=True) as servicebus_client:
            async with servicebus_client:
                # get the Subscription Receiver object for the subscription
                receiver = servicebus_client.get_subscription_receiver(topic_name=self.queue_name,
                                                                       subscription_name=self.subscription_name,
                                                                       max_wait_time=5)
                async with receiver:
                    received_msgs = await receiver.receive_messages(max_wait_time=5, max_message_count=20)
                    for msg in received_msgs:
                        # complete the message so that the message is removed from the subscription
                        await receiver.complete_message(msg)
                    return received_msgs

    async def send_to_topic(self,message_body,application_properties=None):
        # create a Service Bus client using the connection string
        async with ServiceBusClient.from_connection_string(
                conn_str=self.conn_str,
                logging_enable=True) as servicebus_client:
            # Get a Topic Sender object to send messages to the topic
            sender = servicebus_client.get_topic_sender(topic_name=self.topic_name)
            async with sender:
                # Send one message
                message = ServiceBusMessage(message_body, application_properties=application_properties)
                await sender.send_messages(message)
