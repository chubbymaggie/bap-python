#!/usr/bin/env python

"""Lifted ARM instruction"""

from .adt import *
from .asm import *
from .bil import *

class Reg(ADT) : pass
class Nil(Reg) : pass
class GPR(Reg) : pass
class CCR(Reg) : pass

class R0(GPR) : pass
class R1(GPR) : pass
class R2(GPR) : pass
class R3(GPR) : pass
class R4(GPR) : pass
class R5(GPR) : pass
class R6(GPR) : pass
class R7(GPR) : pass
class R8(GPR) : pass
class R9(GPR) : pass
class R10(GPR) : pass
class R11(GPR) : pass
class R12(GPR) : pass
class LR(GPR) : pass
class PC(GPR) : pass
class SP(GPR) : pass

class CPSR(CCR) : pass
class SPSR(CCR) : pass
class ITSTATE(CCR) : pass

class Insn(ADT)     : pass
class Move(Insn)    : pass
class Bits(Insn)    : pass
class Mult(Insn)    : pass
class Mem(Insn)     : pass
class Branch(Insn)  : pass
class Special(Insn) : pass

class ADCri(Move) : pass
class ADCrr(Move) : pass
class ADCrsi(Move) : pass
class ADCrsr(Move) : pass
class ADDri(Move) : pass
class ADDrr(Move) : pass
class ADDrsi(Move) : pass
class ADDrsr(Move) : pass
class ANDri(Move) : pass
class ANDrr(Move) : pass
class ANDrsi(Move) : pass
class ANDrsr(Move) : pass
class BICri(Move) : pass
class BICrr(Move) : pass
class BICrsi(Move) : pass
class BICrsr(Move) : pass
class CMNri(Move) : pass
class CMNzrr(Move) : pass
class CMNzrsi(Move) : pass
class CMNzrsr(Move) : pass
class CMPri(Move) : pass
class CMPrr(Move) : pass
class CMPrsi(Move) : pass
class CMPrsr(Move) : pass
class EORri(Move) : pass
class EORrr(Move) : pass
class EORrsi(Move) : pass
class EORrsr(Move) : pass
class MOVTi16(Move) : pass
class MOVi(Move) : pass
class MOVi16(Move) : pass
class MOVr(Move) : pass
class MOVsi(Move) : pass
class MOVsr(Move) : pass
class MOVPCLR(Move) : pass
class MVNi(Move) : pass
class MVNr(Move) : pass
class MVNsi(Move) : pass
class MVNsr(Move) : pass
class ORRri(Move) : pass
class ORRrr(Move) : pass
class ORRrsi(Move) : pass
class ORRrsr(Move) : pass
class RSBri(Move) : pass
class RSBrr(Move) : pass
class RSBrsi(Move) : pass
class RSBrsr(Move) : pass
class RSCri(Move) : pass
class RSCrr(Move) : pass
class RSCrsi(Move) : pass
class RSCrsr(Move) : pass
class SBCri(Move) : pass
class SBCrr(Move) : pass
class SBCrsi(Move) : pass
class SBCrsr(Move) : pass
class SUBri(Move) : pass
class SUBrr(Move) : pass
class SUBrsi(Move) : pass
class SUBrsr(Move) : pass
class TEQri(Move) : pass
class TEQrr(Move) : pass
class TEQrsi(Move) : pass
class TEQrsr(Move) : pass
class TSTri(Move) : pass
class TSTrr(Move) : pass
class TSTrsi(Move) : pass
class TSTrsr(Move) : pass

class BFC(Bits) : pass
class BFI(Bits) : pass
class PKHTB(Bits) : pass
class RBIT(Bits) : pass
class SBFX(Bits) : pass
class SWPB(Bits) : pass
class SXTAB(Bits) : pass
class SXTAH(Bits) : pass
class SXTB(Bits) : pass
class SXTH(Bits) : pass
class UBFX(Bits) : pass
class UXTAB(Bits) : pass
class UXTAH(Bits) : pass
class UXTB(Bits) : pass
class UXTH(Bits) : pass
class REV(Bits) : pass
class REV16(Bits) : pass
class CLZ(Bits) : pass


class MLA(Mult) : pass
class MLS(Mult) : pass
class MUL(Mult) : pass
class SMLABB(Mult) : pass
class SMLAD(Mult) : pass
class SMLAL(Mult) : pass
class SMLALBT(Mult) : pass
class SMLAWB(Mult) : pass
class SMUAD(Mult) : pass
class SMULBB(Mult) : pass
class SMULL(Mult) : pass
class SMULTB(Mult) : pass
class UMLAL(Mult) : pass
class UMULL(Mult) : pass

class LDMDA(Mem) : pass
class LDMDA_UPD(Mem) : pass
class LDMDB(Mem) : pass
class LDMDB_UPD(Mem) : pass
class LDMIA(Mem) : pass
class LDMIA_UPD(Mem) : pass
class LDMIB(Mem) : pass
class LDMIB_UPD(Mem) : pass
class STMDA(Mem) : pass
class STMDA_UPD(Mem) : pass
class STMDB(Mem) : pass
class STMDB_UPD(Mem) : pass
class STMIA(Mem) : pass
class STMIA_UPD(Mem) : pass
class STMIB(Mem) : pass
class STMIB_UPD(Mem) : pass
class LDRBT_POST_IMM(Mem) : pass
class LDRBT_POST_REG(Mem) : pass
class LDRB_POST_IMM(Mem) : pass
class LDRB_POST_REG(Mem) : pass
class LDRB_PRE_IMM(Mem) : pass
class LDRB_PRE_REG(Mem) : pass
class LDRBi12(Mem) : pass
class LDRBrs(Mem) : pass
class LDRD(Mem) : pass
class LDRD_POST(Mem) : pass
class LDRD_PRE(Mem) : pass
class LDREX(Mem) : pass
class LDREXB(Mem) : pass
class LDREXD(Mem) : pass
class LDREXH(Mem) : pass
class LDRH(Mem) : pass
class LDRHTr(Mem) : pass
class LDRH_POST(Mem) : pass
class LDRH_PRE(Mem) : pass
class LDRSB(Mem) : pass
class LDRSBTr(Mem) : pass
class LDRSB_POST(Mem) : pass
class LDRSB_PRE(Mem) : pass
class LDRSH(Mem) : pass
class LDRSHTi(Mem) : pass
class LDRSHTr(Mem) : pass
class LDRSH_POST(Mem) : pass
class LDRSH_PRE(Mem) : pass
class LDRT_POST_REG(Mem) : pass
class LDR_POST_IMM(Mem) : pass
class LDR_POST_REG(Mem) : pass
class LDR_PRE_IMM(Mem) : pass
class LDR_PRE_REG(Mem) : pass
class LDRi12(Mem) : pass
class LDRrs(Mem) : pass
class STRBT_POST_IMM(Mem) : pass
class STRBT_POST_REG(Mem) : pass
class STRB_POST_IMM(Mem) : pass
class STRB_POST_REG(Mem) : pass
class STRB_PRE_IMM(Mem) : pass
class STRB_PRE_REG(Mem) : pass
class STRBi12(Mem) : pass
class STRBrs(Mem) : pass
class STRD(Mem) : pass
class STRD_POST(Mem) : pass
class STRD_PRE(Mem) : pass
class STREX(Mem) : pass
class STREXB(Mem) : pass
class STREXD(Mem) : pass
class STREXH(Mem) : pass
class STRH(Mem) : pass
class STRHTr(Mem) : pass
class STRH_POST(Mem) : pass
class STRH_PRE(Mem) : pass
class STRT_POST_REG(Mem) : pass
class STR_POST_IMM(Mem) : pass
class STR_POST_REG(Mem) : pass
class STR_PRE_IMM(Mem) : pass
class STR_PRE_REG(Mem) : pass
class STRi12(Mem) : pass
class STRrs(Mem) : pass

class BL(Branch) : pass
class BLX(Branch) : pass
class BLX_pred(Branch) : pass
class BLXi(Branch) : pass
class BL_pred(Branch) : pass
class BX(Branch) : pass
class BX_RET(Branch) : pass
class BX_pred(Branch) : pass
class Bcc(Branch) : pass

class CPS2p(Special) : pass
class DMB(Special) : pass
class DSB(Special) : pass
class HINT(Special) : pass
class MRS(Special) : pass
class MSR(Special) : pass
class PLDi12(Special) : pass
class SVC(Special) : pass


def loads(s):
    return eval(s)
