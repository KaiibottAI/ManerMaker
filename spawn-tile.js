// Need to get this programatically, this doesn't work since this is static for now
const tileFilename = "TILE00.png";
const tilePath = `/modules/hoth/house-tiles/${tileFilename}`;

// Get the current scene
const scene = canvas.scene;
const gridSize = canvas.grid.size;

// Calculate actual top-left grid coordinate, accounting for padding
const x = scene.dimensions.sceneX;
const y = scene.dimensions.sceneY;

const tileData = {
  texture: {
    src: tilePath
  },
  x: scene.dimensions.sceneX,
  y: scene.dimensions.sceneY,
  width: gridSize*5,
  height: gridSize*5,
  rotation: 0,
  z: 100,
  hidden: false,
  locked: false
};

const [newTileDetails] = await canvas.scene.createEmbeddedDocuments("Tile", [tileData]);
// const newTileDetails = new TileDocument(tileData);

ui.notifications.info(`Created new tile ${newTileDetails.id} at ${newTileDetails.x}, ${newTileDetails.y}`)