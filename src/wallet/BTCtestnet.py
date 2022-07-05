from email import header
from ensurepip import version
import logging
import socket
from tarfile import BLOCKSIZE

from numpy import block
from network import NetworkEnvelope, VersionMessage
host = 'testnet.programmingbitcoin.com'
port = 18333
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((host, port))
stream = socket.makefile('rb', None)
verison = VersionMessage()
envelope = NetworkEnvelope(version.command, version.serialize())
socket.sendall(envelope.serialize())
while True:
    new_message = NetworkEnvelope.parse(stream)
    print(new_message)
    
class VerAckMessage:
    command = b 'verack'

    def_init_(self):
        pass

    @classmethod
    def parse(cls,s):
        return cls()

    def serialize(self):
        return b''

class SimpleNode:

    def_init_(self, host, port=None, testnet=False, logging=False):
        if port is None:
            if testnet:
                port = 18333
            else:
                port = 8333
        self.testnet = testnet
        self.logging = logging
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((host, port))
        self.stream = self.socket.makefile('rb', None)

    def send(self, message):
        '''Send a message to the connected node'''
        envelope = NetworkEnvelope(
            message.command, message.serializer(), testnet=self.testnet)
        if self.logging:
            print('sending: {}'.format(envelope))
        self.socket.sendal(envelope.serialize())
    
    def read(self):
        '''Read a message from the socket'''
        envelope = NetworkEnvelope.parse(self.stream, testnet=self.testnet)
        if self.logging:
            print('receiving: {}'.format(envelope))
        return envelope

    def wait_for(self, *message_classes):
        '''Wait for one of the messages in the list'''
        command = None
        command_to_class = {m.command: m for m in message_classes}
        while command not in command_to_class.keys():
            envelope = self.read()
            command = envelope.command
            if command == VersionMessage.command:
                self.send(VerAckMessage())
            elif command == PingMessage.command:
                self.send(PongMessage(envelope.payload))
        return command_to_class[command].parse(envelope.stream())

from network import SimpleNode, VersionMessage
node = SimpleNode('testnet.programmingbitcoin.com', testnet=True)
version = VersionMessage()
node.send(version)
verack_received = False
version_received = False
while not verack_received and not version_received:
    message = node.wait_for(VersionMessage, VerAckMessage)
    if message.command == VerAckMessage.command:
        verack_received = True
    else:
        version_received = True
        node.send(VerAckMessage())

class GetHeadersMessage:
    command = b'getheaders'

    def_init_(self, version=70015, num_hashes=1, start_block=None, end_block=None):
    self.version = version
    self.num_hashes = num_hashes
    if start_block is None:
        raise RuntimeError('a start block is required')
    self.start_block = start_block
    if end_block is None:
        self.end_block = b'\x00' * 32
    else:
        self.end_block = end_block

from io import BytesIO
from block import Block, Genesis_Block
from network import SimpleNode, GetHeadersMessage
node = SimpleNode('mainnet.programmingbitcoin.com', testnet=False)
node.handshake()
genesis = Block.parse(BytesIO(Genesis_Block))
getheaders = GetHeadersMessage(start_block=genesis.hash())
node.send(getheaders)

class HeadersMessage:
    command = b 'headers'

    def_init_(self, blocks):
        self.blocks = blocks 

    @classmethod
    def parse(cls, stream):
        num_headers = read_varint(stream)
        blocks = []
        for _ in range(num_headers):
            blocks.append(Block.parse(steam))
            num_txs = read_varint(stream)
            if num_txs != 0:
                raise Runtimeerror('number of txs not 0')
        return cls(blocks)
from io import BytesIO
from network import SimpleNode, GetHeadersMessage, HeadersMessage
from helper import calculate_new_bits
previous = Block.parse(BytesIO(GENESIS_BLOCK))
first_epoch_timestamp = previous.timestamp
expected_bits = LOWEST_BITS
count = 1
node = SimpleNode ('mainnet.programmingbitcoin.com', testnet=False)
node.handshake()
for _ in range(19):
    getheaders = GetHeadersMessage(start_block=previous.hash())
    node.send(getheaders)
    headers = node.wait_for(HeadersMessage)
    for header in headers.blocks:
        if not header.check_pow():
            raise RuntimeError('bad PoW at block {}'.format(count))
        if header.prev_block != previous.hash():
            raise RuntimeError('discontinuos block at {}'.format(count))
        if count % 2016 == 0:
            time_diff = previous.timestamp - first_epoch_timestamp
            expected_bits = calculate_new_bits(previous.bits, time_diff)
            print(expected_bits.hex())
            first_epoch_timestamp = header.timestamp
        if header.bits != expected_bits:
            raise RuntimeError('bad bits at block {}'.format(count))
        previous = header
        count += 1