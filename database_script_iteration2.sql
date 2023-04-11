CREATE DATABASE IF NOT EXISTS patient_liste;

USE patient_liste;

CREATE TABLE IF NOT EXISTS patient (
  CPR VARCHAR(20) NOT NULL,
  navn VARCHAR(20) NOT NULL,
  alder INT NOT NULL,
  telefon VARCHAR(20) NOT NULL,
  vægt INT NOT NULL,
  co_morbiditeter VARCHAR(50) NOT NULL,
  medicin VARCHAR(20) NOT NULL,
  FEV1 VARCHAR(50) NOT NULL,
  GOLD VARCHAR(50) NOT NULL,
  MRC INT NOT NULL,
  PEF INT NOT NULL
);

INSERT INTO patient (CPR, navn, alder, telefon, vægt, co_morbiditeter, medicin, FEV1, GOLD, MRC, PEF)
VALUES
  ('123456-7890', 'John Doe', 45, '555-1234', 80, 'Hypertension', 'Lisinopril', '2.3', '2', 2, 250),
  ('098765-4321', 'Jane Smith', 32, '555-5678', 60, 'Diabetes', 'Metformin', '2.9', '3', 3, 200),
  ('456789-0123', 'Bob Johnson', 68, '555-2468', 70, 'Osteoporosis', 'Alendronate', '1.8', '1', 1, 180),
  ('987654-3210', 'Alice Brown', 53, '555-3692', 90, 'Asthma', 'Albuterol', '2.1', '2', 2, 220),
  ('654321-0987', 'Mike Davis', 41, '555-1357', 75, 'High Cholesterol', 'Atorvastatin', '2.5', '3', 2, 190),
  ('234567-8901', 'Samantha Wilson', 57, '555-7890', 65, 'Arthritis', 'Ibuprofen', '1.5', '1', 1, 170),
  ('789012-3456', 'David Lee', 29, '555-2468', 85, 'Depression', 'Sertraline', '3.0', '3', 3, 210),
  ('345678-9012', 'Emily Taylor', 46, '555-3692', 55, 'Migraines', 'Sumatriptan', '2.7', '2', 2, 230),
  ('901234-5678', 'Chris Johnson', 63, '555-1357', 77, 'GERD', 'Omeprazole', '1.9', '1', 1, 160),
  ('567890-1234', 'Jessica White', 37, '555-5678', 72, 'None', '', '2.4', '3', 2, 240),
  ('234567-8901', 'Tom Miller', 59, '555-1234', 67, 'None', '', '2.2', '2', 2, 260),
  ('789012-3456', 'Linda Brown', 51, '555-7890', 73, 'Sleep Apnea', 'CPAP', '1.6', '1', 1, 180),
  ('345678-9012', 'Sam Davis', 43, '555-2468', 82, 'Anxiety', 'Lorazepam', '2.8', '3', 3, 220),
  ('901234-5678', 'Kelly Wilson', 55, '555-3692', 62, 'None', '', '1.7', '1', 1, 170)
  ;
  
SELECT distinct * from patient;
