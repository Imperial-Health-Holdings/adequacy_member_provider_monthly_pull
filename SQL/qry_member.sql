/*
	Created by:		Henry Cheng
	Date:			11/30/2021
	Status:			Dev

	This query exports member information from all companies for adequacy report.
	Report is ran the 1st day of every month and dropped to a dedicated folder (handled by Python).
*/

SELECT        
	mc.MEMB_KEYID, 
	mc.MEMB_MPI_NO, 
	mc.MEMBID COLLATE SQL_Latin1_General_CP1_CI_AS AS MID, 
	mc.COMPANY_ID, 
    mc.HPCODE COLLATE SQL_Latin1_General_CP1_CI_AS AS Expr2, 
	mc.SSN COLLATE SQL_Latin1_General_CP1_CI_AS AS Expr3, 
    mc.PATID COLLATE SQL_Latin1_General_CP1_CI_AS AS Expr4, 
	mc.LTRSENT, 
	mc.LTRDATE, 
	mc.LOADDATE, 
	mc.XPDATE, 
    mc.XPSTATUS COLLATE SQL_Latin1_General_CP1_CI_AS AS Expr5, 
	mc.XPTRAN COLLATE SQL_Latin1_General_CP1_CI_AS AS Expr6, 
	mc.OUTLOADDT, 
    mc.Student, 
	mc.RLSHIP, 
	mc.CONTRACTS, 
	mc.STATUS, 
	mc.OTHPRIM, 
    mc.OTHNAME COLLATE SQL_Latin1_General_CP1_CI_AS AS Expr7, 
	mc.OTHCOV, 
	mc.CREATEBY, 
	mc.CREATEDATE, 
    mc.LASTCHANGEBY, 
	mc.LASTCHANGEDATE, 
	mc.ePost_ITS1 COLLATE SQL_Latin1_General_CP1_CI_AS AS Expr8, 
    mc.ePost_ITS2 COLLATE SQL_Latin1_General_CP1_CI_AS AS Expr9, 
	mc.ePost_ITS3 COLLATE SQL_Latin1_General_CP1_CI_AS AS Expr10, 
    mc.ePost_ITS4 COLLATE SQL_Latin1_General_CP1_CI_AS AS Expr11, 
	mc.HoldCodeID, 
	mc.FAMILYNO, 
	mc.MEMBEPOSTITS, 
	mc.ISEZNET1, 
	mc.ISEZNET2, 
	mc.ISEZNET3, 
	mc.ISEZNET4, 
	mc.ISHPGLOBAL, 
	mc.MEMBINDIVIDUALDEATH, 
    mc.MEMBGROUP, 
	mc.POLICYREFERENCEID, 
	mc.DATETIMEQUAL, 
	mc.COVERAGELEVELCODE, 
	mh.OPTHRUDT, 
    mi.ZIP COLLATE SQL_Latin1_General_CP1_CI_AS AS Zip, 
	mi.ADDRESSTYPE
FROM ECD.dbo.MEMB_COMPANY_V mc
	INNER JOIN ECD.dbo.MEMB_HPHISTS_V mh ON mh.MEMB_KEYID = mc.MEMB_KEYID 
	INNER JOIN ECD.dbo.MEMB_CONTACT_INFORMATION_V mi ON mi.MEMB_KEYID = mc.MEMB_KEYID
WHERE
	mh.OPTHRUDT IS NULL
	AND mi.ADDRESSTYPE='home'