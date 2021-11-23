# Data_Cleaning_in_SQL
-- Cleaning Data in SQL Queries

Select *
From students.HousingData

-- Standardize Date Format

Select saleDateConverted, CONVERT(Date,SaleDate)
From students.HousingData


Update students.HousingData
SET SaleDate = CONVERT(Date,SaleDate)

-- If it doesn't Update properly

ALTER TABLE students.HousingData
Add SaleDateConverted Date;

Update students.HousingData
SET SaleDateConverted = CONVERT(Date,SaleDate)


-- Populate Property Address data

Select *
From students.HousingData
--Where PropertyAddress is null
order by ParcelID



Select a.ParcelID, a.PropertyAddress, b.ParcelID, b.PropertyAddress, ISNULL(a.PropertyAddress,b.PropertyAddress)
From students.HousingData a
JOIN students.HousingData b
	on a.ParcelID = b.ParcelID
	AND a.[UniqueID ] <> b.[UniqueID ]
Where a.PropertyAddress is null


Update a
SET PropertyAddress = ISNULL(a.PropertyAddress,b.PropertyAddress)
From students.HousingData a
JOIN students.HousingData b
	on a.ParcelID = b.ParcelID
	AND a.[UniqueID ] <> b.[UniqueID ]
Where a.PropertyAddress is null



-- Breaking out Address into Individual Columns (Address, City, State)


Select PropertyAddress
From students.HousingData
--Where PropertyAddress is null
--order by ParcelID

SELECT
SUBSTRING(PropertyAddress, 1, CHARINDEX(',', PropertyAddress) -1 ) as Address
, SUBSTRING(PropertyAddress, CHARINDEX(',', PropertyAddress) + 1 , LEN(PropertyAddress)) as Address

From students.HousingData


ALTER TABLE students.HousingData
Add PropertySplitAddress Nvarchar(255);

Update students.HousingData
SET PropertySplitAddress = SUBSTRING(PropertyAddress, 1, CHARINDEX(',', PropertyAddress) -1 )


ALTER TABLE students.HousingData
Add PropertySplitCity Nvarchar(255);

Update students.HousingData
SET PropertySplitCity = SUBSTRING(PropertyAddress, CHARINDEX(',', PropertyAddress) + 1 , LEN(PropertyAddress))




Select *
From students.HousingData





Select OwnerAddress
From students.HousingData


Select
PARSENAME(REPLACE(OwnerAddress, ',', '.') , 3)
,PARSENAME(REPLACE(OwnerAddress, ',', '.') , 2)
,PARSENAME(REPLACE(OwnerAddress, ',', '.') , 1)
From students.HousingData



ALTER TABLE students.HousingData
Add OwnerSplitAddress Nvarchar(255);

Update students.HousingData
SET OwnerSplitAddress = PARSENAME(REPLACE(OwnerAddress, ',', '.') , 3)


ALTER TABLE students.HousingData
Add OwnerSplitCity Nvarchar(255);

Update students.HousingData
SET OwnerSplitCity = PARSENAME(REPLACE(OwnerAddress, ',', '.') , 2)

ALTER TABLE students.HousingData
Add OwnerSplitState Nvarchar(255);

Update students.HousingData
SET OwnerSplitState = PARSENAME(REPLACE(OwnerAddress, ',', '.') , 1)

Select *
From students.HousingData


-- Change Y and N to Yes and No in "Sold as Vacant" field


Select Distinct(SoldAsVacant), Count(SoldAsVacant)
From students.HousingData
Group by SoldAsVacant
order by 2




Select SoldAsVacant
, CASE When SoldAsVacant = 'Y' THEN 'Yes'
	   When SoldAsVacant = 'N' THEN 'No'
	   ELSE SoldAsVacant
	   END
From students.HousingData


Update students.HousingData
SET SoldAsVacant = CASE When SoldAsVacant = 'Y' THEN 'Yes'
	   When SoldAsVacant = 'N' THEN 'No'
	   ELSE SoldAsVacant
	   END
From students.HousingData


-- Delete Unused Columns

Select *
From students.HousingData


ALTER TABLE students.HousingData
DROP COLUMN OwnerAddress, TaxDistrict, PropertyAddress, SaleDate
