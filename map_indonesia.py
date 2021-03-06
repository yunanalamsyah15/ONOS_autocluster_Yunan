#!/usr/bin/env python

" Custom Topology to use ONOS Controller"

from mininet.topo import Topo
from mininet.log import setLogLevel, info

class MyTopo( Topo ):

    def addSwitch(self, name, **opts ):
        kwargs = { 'protocols' : 'OpenFlow13'}
        kwargs.update( opts )
        return super(MyTopo, self).addSwitch( name, **kwargs )

    def __init__( self ):
        "Create MyTopo topology..."
        
        # Inisialisasi Topology
        Topo.__init__( self )

        # Tambahkan node, switch, dan host

        info( '*** Add switches\n')
        s1 = self.addSwitch('s1')
        s2 = self.addSwitch('s2')
        s3 = self.addSwitch('s3')
        s4 = self.addSwitch('s4')
        s5 = self.addSwitch('s5')
        s6 = self.addSwitch('s6')
        s7 = self.addSwitch('s7')
        s8 = self.addSwitch('s8')
        s9 = self.addSwitch('s9')
        s10 = self.addSwitch('s10')
        s11 = self.addSwitch('s11')
        s12 = self.addSwitch('s12')
        s13 = self.addSwitch('s13')
        s14 = self.addSwitch('s14')
        s15 = self.addSwitch('s15')
        s16 = self.addSwitch('s16')
        s17 = self.addSwitch('s17')
        s18 = self.addSwitch('s18')
        s19 = self.addSwitch('s19')
        s20 = self.addSwitch('s20')
        s21 = self.addSwitch('s21')
        s22 = self.addSwitch('s22')
        s23 = self.addSwitch('s23')
        s24 = self.addSwitch('s24')
        s25 = self.addSwitch('s25')
        s26 = self.addSwitch('s26')
        s27 = self.addSwitch('s27')
        s28 = self.addSwitch('s28')
        s29 = self.addSwitch('s29')
        s30 = self.addSwitch('s30')
        s31 = self.addSwitch('s31')
        s32 = self.addSwitch('s32')
        s33 = self.addSwitch('s33')
        s34 = self.addSwitch('s34')


        info( '*** Add hosts\n')
        h1 = self.addHost('h1', ip='10.1.0.1')
        h2 = self.addHost('h2', ip='10.1.0.2')
        h3 = self.addHost('h3', ip='10.2.0.3')
        h4 = self.addHost('h4', ip='10.2.0.4')
        h5 = self.addHost('h5', ip='10.3.0.5')
        h6 = self.addHost('h6', ip='10.3.0.6')
        h7 = self.addHost('h7', ip='10.1.0.3')
        h8 = self.addHost('h8', ip='10.1.0.4')
        h9 = self.addHost('h9', ip='10.2.0.1')
        h10 = self.addHost('h10', ip='10.2.0.2')
        h11 = self.addHost('h11', ip='10.3.0.3')
        h12 = self.addHost('h12', ip='10.3.0.4')
        h13 = self.addHost('h13', ip='10.1.0.5')
        h14 = self.addHost('h14', ip='10.1.0.6')
        h15 = self.addHost('h15', ip='10.2.0.7')
        h16 = self.addHost('h16', ip='10.2.0.8')
        h17 = self.addHost('h17', ip='10.3.0.9')

        info( '*** Add links\n')
        self.addLink(s1, h17)
        self.addLink(s2, h16)
        self.addLink(s3, h15)
        self.addLink(s4, h14)
        self.addLink(s5, h13)
        self.addLink(s6, h12)
        self.addLink(s7, h11)
        self.addLink(s8, h10)
        self.addLink(s9, h9)
        self.addLink(s10, h8)
        self.addLink(s11, h7)
        self.addLink(s12, h6)
        self.addLink(s13, h5)
        self.addLink(s14, h4)
        self.addLink(s15, h3)
        self.addLink(s16, h2)
        self.addLink(s17, h1)
        self.addLink(s18, h17)
        self.addLink(s19, h16)
        self.addLink(s20, h15)
        self.addLink(s21, h14)
        self.addLink(s22, h13)
        self.addLink(s23, h12)
        self.addLink(s24, h11)
        self.addLink(s25, h10)
        self.addLink(s26, h9)
        self.addLink(s27, h8)
        self.addLink(s28, h7)
        self.addLink(s29, h6)
        self.addLink(s30, h5)
        self.addLink(s31, h4)
        self.addLink(s32, h3)
        self.addLink(s33, h2)
        self.addLink(s34, h1)
        self.addLink(s1, s34)
        self.addLink(s2, s33)
        self.addLink(s3, s32)
        self.addLink(s4, s31)
        self.addLink(s5, s30)
        self.addLink(s6, s29)
        self.addLink(s7, s28)
        self.addLink(s8, s27)
        self.addLink(s9, s26)
        self.addLink(s10, s25)
        self.addLink(s11, s24)
        self.addLink(s12, s23)
        self.addLink(s13, s22)
        self.addLink(s14, s21)
        self.addLink(s15, s20)
        self.addLink(s16, s19)
        self.addLink(s17, s18)
        self.addLink(s18, s17)
        self.addLink(s19, s16)
        self.addLink(s20, s15)
        self.addLink(s21, s14)
        self.addLink(s22, s13)
        self.addLink(s23, s12)
        self.addLink(s24, s11)
        self.addLink(s25, s10)
        self.addLink(s26, s9)
        self.addLink(s27, s8)
        self.addLink(s28, s7)
        self.addLink(s29, s6)
        self.addLink(s30, s5)
        self.addLink(s31, s4)
        self.addLink(s32, s3)
        self.addLink(s33, s2)
        self.addLink(s34, s1)

topos = { 'mytopo': ( lambda: MyTopo() ) }
    
if __name__ == '__main__':
    from onosnet import run
    run( MyTopo() )
