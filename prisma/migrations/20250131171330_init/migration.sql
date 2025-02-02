/*
  Warnings:

  - You are about to alter the column `open` on the `StockData` table. The data in that column could be lost. The data in that column will be cast from `Decimal(65,2)` to `Decimal(65,30)`.
  - You are about to alter the column `high` on the `StockData` table. The data in that column could be lost. The data in that column will be cast from `Decimal(65,2)` to `Decimal(65,30)`.
  - You are about to alter the column `low` on the `StockData` table. The data in that column could be lost. The data in that column will be cast from `Decimal(65,2)` to `Decimal(65,30)`.
  - You are about to alter the column `close` on the `StockData` table. The data in that column could be lost. The data in that column will be cast from `Decimal(65,2)` to `Decimal(65,30)`.

*/
-- AlterTable
ALTER TABLE "StockData" ALTER COLUMN "open" SET DATA TYPE DECIMAL(65,2),
ALTER COLUMN "high" SET DATA TYPE DECIMAL(65,2),
ALTER COLUMN "low" SET DATA TYPE DECIMAL(65,2),
ALTER COLUMN "close" SET DATA TYPE DECIMAL(65,2);

-- RenameIndex
ALTER INDEX "StockData_date_key" RENAME TO "StockData_datetime_key";
