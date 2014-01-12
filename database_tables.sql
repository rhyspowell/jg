CREATE TABLE IF NOT EXISTS `jumpgate`.`pilots` (
  `idpilots` INT NOT NULL AUTO_INCREMENT,
  `pilots_name` VARCHAR(50) NULL,
  PRIMARY KEY (`idpilots`),
  UNIQUE INDEX `idpilots_UNIQUE` (`idpilots` ASC),
  UNIQUE INDEX `pilots_name_UNIQUE` (`pilots_name` ASC))
ENGINE = InnoDB