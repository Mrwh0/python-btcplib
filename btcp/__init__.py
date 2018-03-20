# Copyright (C) 2012-2016 The python-bitcoinlib developers
#
# This file is part of python-bitcoinlib.
#
# It is subject to the license terms in the LICENSE file found in the top-level
# directory of this distribution.
#
# No part of python-bitcoinlib, including this file, may be copied, modified,
# propagated, or distributed except according to the terms contained in the
# LICENSE file.

from __future__ import absolute_import, division, print_function, unicode_literals

import btcp.core

# Note that setup.py can break if __init__.py imports any external
# dependencies, as these might not be installed when setup.py runs. In this
# case __version__ could be moved to a separate version.py and imported here.
__version__ = '0.7.1-SNAPSHOT'

class MainParams(btcp.core.CoreMainParams):
    MESSAGE_START = b'\xa8\xea\xa2\xcd'
    DEFAULT_PORT = 7933
    RPC_PORT = 7932

    DNS_SEEDS = ('btcprivate.org', 'dnsseed.btcpprivate.org')
    # PUBKEY_ADDR: first 2 characters, when base58 encoded, are "t1"
    # SCRIPT_ADDR: first 2 characters, when base58 encoded, are "t3"
    # SECRET_KEY: the first character, when base58 encoded, is "5" or "K" or "L" (as in Bitcoin)
    # ZCPAYMENT_ADDRRESS: guarantees the first 2 characters, when base58 encoded, are "zc"
    BASE58_PREFIXES = {'PUBKEY_ADDR':b'\x13\x25',
                       'SCRIPT_ADDR':b'\x13\xAF',
                       'SECRET_KEY' :128,
                       'ZCPAYMENT_ADDRRESS': b'\x16\xA8'}

class TestNetParams(btcp.core.CoreTestNetParams):
    MESSAGE_START = b'\xf6\x1b\xf6\xd6'
    DEFAULT_PORT = 17933
    RPC_PORT = 17932
    #no testnet dnsseed YET! WOP!
    DNS_SEEDS = ()
    # PUBKEY_ADDR: first 2 characters, when base58 encoded, are "tm"
    # SCRIPT_ADDR: first 2 characters, when base58 encoded, are "t2"
    # SECRET_KEY: the first character, when base58 encoded, is "9" or "c" (as in Bitcoin)
    # ZCPAYMENT_ADDRRESS: guarantees the first 2 characters, when base58 encoded, are "zt"
    BASE58_PREFIXES = {'PUBKEY_ADDR':b'\x19\x57',
                       'SCRIPT_ADDR':b'\x19\xE0',
                       'SECRET_KEY' :239, # b'\xEF',
                       'ZCPAYMENT_ADDRRESS': b'\x16\xC0'}

class RegTestParams(btcp.core.CoreRegTestParams):
    MESSAGE_START = b'\xaa\xe8\x3f\x5f'
    DEFAULT_PORT = 17944
    RPC_PORT = 17943
    DNS_SEEDS = ()
    BASE58_PREFIXES = {'PUBKEY_ADDR':b'\x19\x57',
                       'SCRIPT_ADDR':b'\x19\xE0',
                       'SECRET_KEY' :239, # b'\xEF',
                       'ZCPAYMENT_ADDRRESS': b'\x16\xC0'}

"""Master global setting for what chain params we're using.

However, don't set this directly, use SelectParams() instead so as to set the
btcp.core.params correctly too.
"""
#params = btcp.core.coreparams = MainParams()
params = MainParams()

def SelectParams(name):
    """Select the chain parameters to use

    name is one of 'mainnet', 'testnet', or 'regtest'

    Default chain is 'mainnet'
    """
    global params
    btcp.core._SelectCoreParams(name)
    if name == 'mainnet':
        params = btcp.core.coreparams = MainParams()
    elif name == 'testnet':
        params = btcp.core.coreparams = TestNetParams()
    elif name == 'regtest':
        params = btcp.core.coreparams = RegTestParams()
    else:
        raise ValueError('Unknown chain %r' % name)
