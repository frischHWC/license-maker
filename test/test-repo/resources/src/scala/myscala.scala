/**
 * Licensed to the Apache Software Foundation (ASF) under one
 * or more contributor license agreements.  See the NOTICE file
 * distributed with this work for additional information
 * regarding copyright ownership.  The ASF licenses this file
 * to you under the Apache License, Version 2.0 (the
 * "License"); you may not use this file except in compliance
 * with the License.  You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */package com.cloudera.frisch.publishtoatlas

import com.cloudera.frisch.publishtoatlas.config.StandardConfig
import org.apache.logging.log4j.scala.Logging


object App extends Logging {

  /**
    * Main function that launches treatment
    * @param args Not needed
    */
  def main(args : Array[String]) {

    logger.info("Starting Program : " + StandardConfig.appName)

    AtlasSetup.setupAtlasConf()

    for(i <- Range(1,2)) {
     AtlasExamplesEntities.createAtlasEntityWithInt(i)
    }

    logger.info("Finished Program")
  }
