"""
FIX 4.4 Message Types

This module defines the standard FIX 4.4 message types as an enum.
"""
from enum import Enum, auto

class MessageType(Enum):
    """FIX 4.4 Message Types"""
    # Administrative Messages
    Heartbeat = "0"
    TestRequest = "1"
    ResendRequest = "2"
    Reject = "3"
    SequenceReset = "4"
    Logout = "5"
    Logon = "A"
    
    # Application Messages - Session
    BusinessMessageReject = "j"
    
    # Application Messages - Order Handling
    NewOrderSingle = "D"
    NewOrderList = "E"
    OrderCancelRequest = "F"
    OrderCancelReplaceRequest = "G"
    OrderStatusRequest = "H"
    OrderMassStatusRequest = "AF"
    OrderMassCancelRequest = "q"
    OrderMassCancelReport = "r"
    RequestForPositions = "AN"
    RequestForPositionsAck = "AO"
    AllocationInstruction = "J"
    AllocationReport = "AS"
    AllocationInstructionAck = "P"
    AllocationReportAck = "AT"
    
    # Application Messages - Market Data
    MarketDataRequest = "V"
    MarketDataSnapshotFullRefresh = "W"
    MarketDataIncrementalRefresh = "X"
    MarketDataRequestReject = "Y"
    SecurityDefinitionRequest = "c"
    SecurityDefinition = "d"
    SecurityStatusRequest = "e"
    SecurityStatus = "f"
    SecurityTypeRequest = "v"
    SecurityTypes = "w"
    SecurityListRequest = "x"
    SecurityList = "y"
    DerivativeSecurityListRequest = "z"
    DerivativeSecurityList = "AA"
    
    # Application Messages - Quotation
    Quote = "S"
    QuoteCancel = "Z"
    QuoteStatusRequest = "a"
    QuoteStatusReport = "AI"
    QuoteRequest = "R"
    QuoteRequestReject = "AG"
    QuoteResponse = "AJ"
    MassQuote = "i"
    MassQuoteAcknowledgement = "b"
    
    # Application Messages - Trade
    ExecutionReport = "8"
    DontKnowTrade = "Q"
    OrderCancelReject = "9"
    
    # Application Messages - Trade Capture
    TradeCaptureReportRequest = "AD"
    TradeCaptureReportRequestAck = "AQ"
    TradeCaptureReport = "AE"
    TradeCaptureReportAck = "AR"
    
    # Application Messages - Positions
    PositionMaintenanceRequest = "AL"
    PositionMaintenanceReport = "AM"
    PositionReport = "AP"
    
    # Application Messages - Registration
    RegistrationInstructions = "o"
    RegistrationInstructionsResponse = "p"
    
    # Application Messages - Miscellaneous
    Email = "C"
    News = "B"
    ListExecute = "L"
    ListCancelRequest = "K"
    ListStatus = "N"
    ListStatusRequest = "M"
    ListStrikePrice = "m"
    
    # Application Messages - Cross Orders
    NewOrderCross = "s"
    CrossOrderCancelReplaceRequest = "t"
    CrossOrderCancelRequest = "u"
    MultilegOrderCancelReplace = "AC"
    NewOrderMultileg = "AB"
    
    # Application Messages - Network
    NetworkCounterpartySystemStatusRequest = "BC"
    NetworkCounterpartySystemStatusResponse = "BD"
    
    # Application Messages - Collateral
    CollateralRequest = "AX"
    CollateralAssignment = "AY"
    CollateralResponse = "AZ"
    CollateralReport = "BA"
    CollateralInquiry = "BB"
    CollateralInquiryAck = "BG"
    
    # Application Messages - Settlement
    SettlementInstructions = "T"
    SettlementInstructionRequest = "AV"
    
    # Application Messages - Confirmation
    Confirmation = "AK"
    ConfirmationRequest = "BH"
    ConfirmationAck = "AU"
    
    # Application Messages - Trading Session
    TradingSessionStatusRequest = "g"
    TradingSessionStatus = "h"
    
    # Application Messages - Allocation
    AssignmentReport = "BK"
    
    # Application Messages - Bidding
    BidRequest = "k"
    BidResponse = "l"
    
    # Application Messages - Advertisement
    Advertisement = "7"
    
    # Non-FIX messages
    XMLNonFIX = "n" 