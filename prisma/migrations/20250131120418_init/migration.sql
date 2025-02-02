-- CreateTable
CREATE TABLE "StockData" (
    "datetime" TIMESTAMP(3) NOT NULL,
    "open" DECIMAL(65,2) NOT NULL,
    "high" DECIMAL(65,2) NOT NULL,
    "low" DECIMAL(65,2) NOT NULL,
    "close" DECIMAL(65,2) NOT NULL,
    "volume" INTEGER NOT NULL
);

-- CreateIndex
CREATE UNIQUE INDEX "StockData_date_key" ON "StockData"("datetime");
