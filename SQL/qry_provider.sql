/*
	Created by:		Henry Cheng
	Date:			11/30/2021
	Status:			Dev

	This query exports provider information from all companies for adequacy report.
	Report is ran the 1st day of every month and dropped to a dedicated folder (handled by Python).
*/

/* IICT */
SELECT DISTINCT 
	pm.FIRSTNAME, 
	pm.LASTNAME, 
	pm.MI, 
	pm.FULLNAME, 
	pm.REV_FULLNAME, 
    pm.COMPANY_ID COLLATE SQL_Latin1_General_CP1_CI_AS AS COMPANY, 
	pm.FROMDATE, 
	pm.TERMDATE, 
	ps.SPECCODE, 
    ps.SPECDESCR, 
	pv.VENDOR COLLATE SQL_Latin1_General_CP1_CI_AS AS Vendor, 
	vm.VENDORNM, 
	pv.THRUDATE, 
    vm.VENDORNM1, 
	vm.VENDORNM2, 
	pa.ADDTYPE COLLATE SQL_Latin1_General_CP1_CI_AS AS AddressType, 
    pa.ZIP COLLATE SQL_Latin1_General_CP1_CI_AS AS ZIP, 
	pa.EXPDATE, 
	pi.OUTSIDEID COLLATE SQL_Latin1_General_CP1_CI_AS AS Affiliation
FROM IICT.dbo.VEND_MASTERS_V vm
	INNER JOIN IICT.dbo.PROV_VENDINFO pv ON vm.VENDORID = pv.VENDOR COLLATE SQL_Latin1_General_CP1_CI_AS 
	INNER JOIN IICT.dbo.PROV_ADDINFO pa ON pv.PROV_KEYID = pa.PROV_KEYID 
	LEFT OUTER JOIN IICT.dbo.PROV_IDINFO_V pi ON pv.PROV_KEYID = pi.PROV_KEYID 
	RIGHT OUTER JOIN IICT.dbo.PROV_MASTERS pm ON pv.PROV_KEYID = pm.PROV_KEYID 
	LEFT OUTER JOIN IICT.dbo.PROV_SPECINFO_V ps ON pm.PROV_KEYID = ps.PROV_KEYID
WHERE        
	pm.CONTRACT IN ('1', '2', '6', '7')
	AND pa.EXPDATE IS NULL
	AND pm.TERMDATE IS NULL

/* IMPERIAL */
UNION ALL
SELECT DISTINCT 
	pm.FIRSTNAME, 
	pm.LASTNAME, 
	pm.MI, 
	pm.FULLNAME, 
	pm.REV_FULLNAME, 
    pm.COMPANY_ID COLLATE SQL_Latin1_General_CP1_CI_AS AS COMPANY, 
	pm.FROMDATE, 
	pm.TERMDATE, 
	ps.SPECCODE, 
    ps.SPECDESCR, 
	pv.VENDOR COLLATE SQL_Latin1_General_CP1_CI_AS AS Vendor, 
	vm.VENDORNM, 
	pv.THRUDATE, 
    vm.VENDORNM1, 
	vm.VENDORNM2, 
	pa.ADDTYPE COLLATE SQL_Latin1_General_CP1_CI_AS AS AddressType, 
    pa.ZIP COLLATE SQL_Latin1_General_CP1_CI_AS AS ZIP, 
	pa.EXPDATE, 
	pi.OUTSIDEID COLLATE SQL_Latin1_General_CP1_CI_AS AS Affiliation
FROM IMPERIAL.dbo.VEND_MASTERS_V vm
	INNER JOIN IMPERIAL.dbo.PROV_VENDINFO pv ON vm.VENDORID = pv.VENDOR COLLATE SQL_Latin1_General_CP1_CI_AS 
	INNER JOIN IMPERIAL.dbo.PROV_ADDINFO pa ON pv.PROV_KEYID = pa.PROV_KEYID 
	LEFT OUTER JOIN IMPERIAL.dbo.PROV_IDINFO_V pi ON pv.PROV_KEYID = pi.PROV_KEYID 
	RIGHT OUTER JOIN IMPERIAL.dbo.PROV_MASTERS pm ON pv.PROV_KEYID = pm.PROV_KEYID 
	LEFT OUTER JOIN IMPERIAL.dbo.PROV_SPECINFO_V ps ON pm.PROV_KEYID = ps.PROV_KEYID
WHERE        
	pm.CONTRACT IN ('1', '2', '6', '7')
	AND pa.EXPDATE IS NULL

/* IHHMG */
UNION ALL
SELECT DISTINCT 
	pm.FIRSTNAME, 
	pm.LASTNAME, 
	pm.MI, 
	pm.FULLNAME, 
	pm.REV_FULLNAME, 
    pm.COMPANY_ID COLLATE SQL_Latin1_General_CP1_CI_AS AS COMPANY, 
	pm.FROMDATE, 
	pm.TERMDATE, 
	ps.SPECCODE, 
    ps.SPECDESCR, 
	pv.VENDOR COLLATE SQL_Latin1_General_CP1_CI_AS AS Vendor, 
	vm.VENDORNM, 
	pv.THRUDATE, 
    vm.VENDORNM1, 
	vm.VENDORNM2, 
	pa.ADDTYPE COLLATE SQL_Latin1_General_CP1_CI_AS AS AddressType, 
    pa.ZIP COLLATE SQL_Latin1_General_CP1_CI_AS AS ZIP, 
	pa.EXPDATE, 
	pi.OUTSIDEID COLLATE SQL_Latin1_General_CP1_CI_AS AS Affiliation
FROM IHHMG.dbo.VEND_MASTERS_V vm
	INNER JOIN IHHMG.dbo.PROV_VENDINFO pv ON vm.VENDORID = pv.VENDOR COLLATE SQL_Latin1_General_CP1_CI_AS 
	INNER JOIN IHHMG.dbo.PROV_ADDINFO pa ON pv.PROV_KEYID = pa.PROV_KEYID 
	LEFT OUTER JOIN IHHMG.dbo.PROV_IDINFO_V pi ON pv.PROV_KEYID = pi.PROV_KEYID 
	RIGHT OUTER JOIN IHHMG.dbo.PROV_MASTERS pm ON pv.PROV_KEYID = pm.PROV_KEYID 
	LEFT OUTER JOIN IHHMG.dbo.PROV_SPECINFO_V ps ON pm.PROV_KEYID = ps.PROV_KEYID
WHERE        
	pm.CONTRACT IN ('1', '2', '6', '7')
	AND pa.EXPDATE IS NULL

/* H2793 */
UNION ALL
SELECT DISTINCT 
	pm.FIRSTNAME, 
	pm.LASTNAME, 
	pm.MI, 
	pm.FULLNAME, 
	pm.REV_FULLNAME, 
    pm.COMPANY_ID COLLATE SQL_Latin1_General_CP1_CI_AS AS COMPANY, 
	pm.FROMDATE, 
	pm.TERMDATE, 
	ps.SPECCODE, 
    ps.SPECDESCR, 
	pv.VENDOR COLLATE SQL_Latin1_General_CP1_CI_AS AS Vendor, 
	vm.VENDORNM, 
	pv.THRUDATE, 
    vm.VENDORNM1, 
	vm.VENDORNM2, 
	pa.ADDTYPE COLLATE SQL_Latin1_General_CP1_CI_AS AS AddressType, 
    pa.ZIP COLLATE SQL_Latin1_General_CP1_CI_AS AS ZIP, 
	pa.EXPDATE, 
	pi.OUTSIDEID COLLATE SQL_Latin1_General_CP1_CI_AS AS Affiliation
FROM H2793.dbo.VEND_MASTERS_V vm
	INNER JOIN H2793.dbo.PROV_VENDINFO pv ON vm.VENDORID = pv.VENDOR COLLATE SQL_Latin1_General_CP1_CI_AS 
	INNER JOIN H2793.dbo.PROV_ADDINFO pa ON pv.PROV_KEYID = pa.PROV_KEYID 
	LEFT OUTER JOIN H2793.dbo.PROV_IDINFO_V pi ON pv.PROV_KEYID = pi.PROV_KEYID 
	RIGHT OUTER JOIN H2793.dbo.PROV_MASTERS pm ON pv.PROV_KEYID = pm.PROV_KEYID 
	LEFT OUTER JOIN H2793.dbo.PROV_SPECINFO_V ps ON pm.PROV_KEYID = ps.PROV_KEYID
WHERE        
	pm.CONTRACT IN ('1', '2', '6', '7')
	AND pa.EXPDATE IS NULL